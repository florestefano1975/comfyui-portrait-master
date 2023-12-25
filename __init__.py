# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Modified by Steven Chen
# Version: 2.0
# https://stefanoflore.it
# https://ai-wiz.art

import json
import os

script_dir = os.path.dirname(__file__)

# read txt file
CONFIG_MAPPINGS = {}
DISPLAY_CONFIG_DICT = {}
PARSE_CONFIG_DICT = {}
CONFIG_ITEMS = []


def sys_init(language="cn"):
    for filename in os.listdir(os.path.join(script_dir, "lists")):
        if filename.endswith(".json"):
            try:
                with open(os.path.join(script_dir, "lists", filename), 'r') as file:
                    json_obj = json.load(file)
                    meta_info = json_obj["meta_info"]
                    config_type = meta_info["config_type"]
                    CONFIG_MAPPINGS[config_type] = json_obj
            except Exception as e:
                print(f"Portrait Master: error loading {filename}: {e}")
    print("Portrait Master: loaded all json files in the lists folder")
    print(f"Got configs: {CONFIG_MAPPINGS.keys()}")
    build_config_dict(language)


def build_config_dict(language="cn"):
    entries = [entry for entry in CONFIG_MAPPINGS.values()
               if (entry["meta_info"].get("position", -1) > 0) and (entry["meta_info"].get("replica", -1) > 0)]
    entries.sort(key=lambda x: x["meta_info"]["position"])

    for config_dict in entries:
        meta_info = config_dict["meta_info"]
        values = config_dict["values"]

        config_type = meta_info.get("config_type", "").strip()
        if 'language' == config_type:
            language = values["default_value"]

        replica = meta_info.get("replica", 0)
        if not (config_type or replica):
            continue

        base_config_display, config_details, config_meta = build_config_details(config_dict, language)
        CONFIG_ITEMS.append(base_config_display)
        DISPLAY_CONFIG_DICT.update(config_details)
        PARSE_CONFIG_DICT.update(config_meta)
    print(f"Portrait Master: built config details: "
          f"「{CONFIG_ITEMS}」,"
          f"「{DISPLAY_CONFIG_DICT.keys()}」, "
          f"「{PARSE_CONFIG_DICT.keys()}」")


def build_config_details(config_dict, language):
    meta_info = config_dict["meta_info"]
    values = config_dict["values"]
    weight = config_dict["weight"]
    mix = config_dict["mix"]

    config_type = meta_info['config_type'].strip()
    replica = meta_info['replica']
    base_config_display = meta_info['display'][language]
    value_type = meta_info.get("value_type", "").strip().lower()

    config_details = {}
    config_meta = {}
    is_mix = len(mix) > 0
    single_config = (1 == replica)
    for i in range(replica):
        if single_config:
            config_name = config_type
            config_display = base_config_display
        else:
            config_name = f"{config_type}_{str(i)}"
            config_display = f"{base_config_display}_{str(i)}"

        default_value = ''
        option_mapping = {}
        if "list" == value_type:
            default_value = values.get('default', '-')
            option_list = values.get(language, [])
            option_display_list = [default_value]
            for option in option_list:
                if isinstance(option, str):
                    option_mapping[option] = option
                    option_display_list.append(option)
                else:
                    display_option = option["display"]
                    option_mapping[display_option] = option["key"]
                    option_display_list.append(display_option)

            config_details[config_display] = (option_display_list, {
                "default": option_display_list[0],
            })

        elif "float" == value_type:
            default_value = values.get('default', 0.1)
            config_details[config_display] = ("FLOAT", {
                "default": default_value,
                "min": values.get('min', 0),
                "max": values.get('max', 1),
                "step": values.get('step', 0.05),
                "display": "slider",
            })

        elif "int" == value_type:
            default_value = values.get('default', 1)
            config_details[config_display] = ("INT", {
                "default": int(default_value),
                "min": int(values.get('min', 0)),
                "max": int(values.get('max', 10)),
                "step": int(values.get('step', 1)),
                "display": "slider",
            })

        elif "string" == value_type:
            config_details[config_display] = ("STRING", {
                "multiline": values.get('multiline', True),
                "default": values['default']
            })

        config_meta[config_display] = {
            'option_mapping': option_mapping,
            'config_type': config_type,
            'value_type': value_type,
            'default': default_value,
            'prefix': values.get('prefix', ''),
            'suffix': values.get('suffix', ''),
            'name': config_name,
            'weight': weight,
            'mix': is_mix,
        }

        weight_changeable = weight.get("changeable", False)
        if weight_changeable and single_config:
            config_details[f"{config_display}_weight"] = ("FLOAT", {
                "default": weight['default'],
                "min": weight['min'],
                "max": weight['max'],
                "step": weight['step'],
                "display": "slider",
            })

    if is_mix:
        config_details[f"{base_config_display}_mix"] = ("FLOAT", mix)

    return base_config_display, config_details, config_meta


class PortraitMasterI18N:

    def __init__(self):
        sys_init(language=self.SYS_LANGUAGE)
        pass

    @classmethod
    def INPUT_TYPES(s):

        return {
            "required": DISPLAY_CONFIG_DICT
        }

    RETURN_TYPES = ("STRING", "STRING",)
    RETURN_NAMES = ("positive", "negative",)
    FUNCTION = "handler"
    CATEGORY = "AI WizArt"
    SYS_LANGUAGE = "cn"

    def process_key(self, item):
        parts = item.split('_')
        if parts[-1].isdigit() or parts[-1] == 'weight':
            return '_'.join(parts[:-1])
        else:
            return item

    def handler(self, **kwargs):

        # group the keys for each attributes
        keys_mapping = {}
        for key in kwargs.keys():
            if '_' not in key:
                continue

            core_key = self.process_key(key)
            if core_key == key:
                keys_mapping[key] = [key]
            else:
                keys_mapping.setdefault(core_key, []).append(key)
        print(f"Portrait Master: keys_mapping: 「{keys_mapping}」，kwargs: 「{kwargs}」")

        handled_keys = []
        prompt_items = []
        for param_key in CONFIG_ITEMS:
            # need special logic to handle the 'prompt_prefix' and 'prompt_suffix'
            if ('prompt' in param_key) or ('language' in param_key):
                continue

            key_list = keys_mapping.get(param_key, [])
            if not key_list:
                continue

            for key in key_list:
                config_meta = PARSE_CONFIG_DICT.get(param_key, None)
                if (not config_meta) or (key in handled_keys) or ('mix' in key):
                    continue

                # record the handled key
                handled_keys.append(key)

                value_type = config_meta['value_type']
                option_mapping = config_meta['option_mapping']
                prefix = config_meta.get('prefix', '')
                suffix = config_meta.get('suffix', '')
                default = config_meta['default']
                weight = config_meta['weight']
                mix = config_meta['mix']

                value = kwargs.get(key, default)
                if value == default:
                    continue

                if "list" == value_type:
                    display = option_mapping.get(value, '')
                    if not display:
                        continue

                    ori_option = option_mapping[display]
                    if not mix:
                        prompt_item = f"{prefix}{ori_option}{suffix}"
                        config_weight = kwargs.get(f"{param_key}_weight", weight['default'])
                        if config_weight != weight['default']:
                            prompt_item = f"({prompt_item}:{config_weight})"
                        prompt_items.append(prompt_item)
                    else:
                        prompt_item = ''
                        parts = key.split('_')
                        if parts[-1].isdigit():
                            num = int(parts[-1])
                            mix_items = []
                            for i in range(num + 2):
                                tmp_key = f"{'_'.join(parts[:-1])}_{i}"
                                tmp_value = kwargs.get(tmp_key, default)
                                if tmp_value == default:
                                    continue

                                handled_keys.append(tmp_key)
                                mix_items.append(tmp_value)
                            mix_rate = mix.get('rate', 0.5)
                            tmp_item = ":".join(mix_items + [str(mix_rate)])
                            prompt_item = f"{prefix}[{tmp_item}]{suffix}"
                        prompt_items.append(prompt_item)

                elif isinstance(value, (int, float)):
                    prompt_item = f"{prefix}{param_key}{suffix}"
                    config_weight = kwargs.get(f"{param_key}_weight", weight['default'])
                    if config_weight != weight['default']:
                        prompt_item = f"({prompt_item}:{config_weight})"
                    prompt_items.append(prompt_item)

        # handle the prompt_prefix and prompt_suffix
        prompt_prefix = kwargs.get('prompt_prefix', '')
        prompt_suffix = kwargs.get('prompt_suffix', '')
        prompt_items = [prompt_prefix] + prompt_items + [prompt_suffix]
        prompt = ', '.join([item for item in prompt_items if item])

        # handle language
        language = kwargs.get('language', self.SYS_LANGUAGE)
        if language != self.SYS_LANGUAGE:
            self.SYS_LANGUAGE = language

        negative_prompt = kwargs.get('negative_prompt', '')
        print(f"Portrait Master: prompt: [{prompt}], negative_prompt: [{negative_prompt}]")
        return (prompt, negative_prompt,)


sys_init(PortraitMasterI18N().SYS_LANGUAGE)

NODE_CLASS_MAPPINGS = {
    "PortraitMaster": PortraitMasterI18N
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PortraitMaster": "Steven version of Portrait Master"
}
