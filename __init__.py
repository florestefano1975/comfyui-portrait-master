# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Version: 3.5.0
# https://stefanoflore.it
# https://ai-wiz.art

import os
import random
import json
from .legacy import PortraitMaster
from .utils import pmReadTxt, applyWeight

script_dir = os.path.dirname(__file__)
presets_dir = os.path.join(script_dir, "presets")

# global vars

rand_opt = 'random 🎲'

# Load lists

def load_lists():
    lists = {}
    list_names = [
        "shot", "gender", "face_shape", "face_expression", "nationality", "hair_style", "light_type", "light_direction", "eyes_color", "eyes_shape", "beard_color", "hair_color", "hair_length", "body_type", "beard", "model_pose", "style", "lips_shape", "lips_color", "makeup", "clothes", "age", "makeup_color", "female_lingerie", "breast_size", "butt_size"
    ]
    for name in list_names:
        list_path = os.path.join(script_dir, f"lists/{name}_list.txt")
        if os.path.exists(list_path):
            lists[name] = pmReadTxt(list_path)
            lists[name].sort()
        else:
            lists[name] = []
    return lists

lists = load_lists()

# Load presets
def get_presets(preset_class):
    if not os.path.exists(presets_dir):
        return []

    class_presets_dir = os.path.join(presets_dir, preset_class)
    if not os.path.exists(class_presets_dir):
        return []

    files = [f for f in os.listdir(class_presets_dir) if f.endswith('.json')]
    return [os.path.splitext(f)[0] for f in files]

# Generic preset logic handler
def handle_presets(node_instance, **kwargs):
    params = {k: v for k, v in kwargs.items()}

    # Saving
    if params.get("save_preset") and params.get("save_preset_as"):
        preset_name = params["save_preset_as"].strip()
        if preset_name:
            preset_data = {k: v for k, v in params.items() if k not in ['text_in', 'seed', 'load_preset', 'save_preset_as', 'save_preset', '_presets_separator']}

            class_presets_dir = os.path.join(presets_dir, node_instance.preset_class)
            if not os.path.exists(class_presets_dir):
                os.makedirs(class_presets_dir)

            filepath = os.path.join(class_presets_dir, f"{preset_name}.json")
            with open(filepath, 'w') as f:
                json.dump(preset_data, f, indent=4)
            print(f"Saved preset to {filepath}")

    # Loading
    if params.get("load_preset") and params.get("load_preset") != "-- disabled --":
        preset_name = params["load_preset"]
        filepath = os.path.join(presets_dir, node_instance.preset_class, f"{preset_name}.json")
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                preset_data = json.load(f)
            params.update(preset_data)
            print(f"Loaded preset from {filepath}")

    return params

# Portrait Master Base Character

class PortraitMasterBaseCharacter:
    preset_class = "BaseCharacter"

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        preset_files = get_presets(s.preset_class)

        return {
            "optional": {"text_in": ("STRING", {"forceInput": True}), "seed": ("INT", {"forceInput": False})},
            "required": {
                "shot": (['-'] + [rand_opt] + lists['shot'], {"default": '-'}),
                "shot_weight": ("FLOAT", {"default": 1, "step": 0.05, "min": 0, "max": max_float_value, "display": "slider"}),
                "gender": (['-'] + [rand_opt] + lists['gender'], {"default": '-'}),
                "androgynous": ("FLOAT", {"default": 0, "min": 0, "max": max_float_value, "step": 0.05, "display": "slider"}),
                "ugly": ("FLOAT", {"default": 0, "min": 0, "max": max_float_value, "step": 0.05, "display": "slider"}),
                "ordinary_face": ("FLOAT", {"default": 0, "min": 0, "max": max_float_value, "step": 0.05, "display": "slider"}),
                "age": (['-'] + [rand_opt] + lists['age'], {"default": '-'}),
                "nationality_1": (['-'] + [rand_opt] + lists['nationality'], {"default": '-'}),
                "nationality_2": (['-'] + [rand_opt] + lists['nationality'], {"default": '-'}),
                "nationality_mix": ("FLOAT", {"default": 0.5, "min": 0, "max": 1, "step": 0.05, "display": "slider"}),
                "body_type": (['-'] + [rand_opt] + lists['body_type'], {"default": '-'}),
                "body_type_weight": ("FLOAT", {"default": 1, "step": 0.05, "min": 0, "max": max_float_value, "display": "slider"}),
                "breast_size": (['-'] + [rand_opt] + lists['breast_size'], {"default": '-'}),
                "breast_size_weight": ("FLOAT", {"default": 1, "step": 0.05, "min": 0, "max": max_float_value, "display": "slider"}),
                "butt_size": (['-'] + [rand_opt] + lists['butt_size'], {"default": '-'}),
                "butt_size_weight": ("FLOAT", {"default": 1, "step": 0.05, "min": 0, "max": max_float_value, "display": "slider"}),
                "eyes_color": (['-'] + [rand_opt] + lists['eyes_color'], {"default": '-'}),
                "eyes_shape": (['-'] + [rand_opt] + lists['eyes_shape'], {"default": '-'}),
                "lips_color": (['-'] + [rand_opt] + lists['lips_color'], {"default": '-'}),
                "lips_shape": (['-'] + [rand_opt] + lists['lips_shape'], {"default": '-'}),
                "facial_expression": (['-'] + [rand_opt] + lists['face_expression'], {"default": '-'}),
                "facial_expression_weight": ("FLOAT", {"default": 1, "step": 0.05, "min": 0, "max": max_float_value, "display": "slider"}),
                "face_shape": (['-'] + [rand_opt] + lists['face_shape'], {"default": '-'}),
                "face_shape_weight": ("FLOAT", {"default": 1, "step": 0.05, "min": 0, "max": max_float_value, "display": "slider"}),
                "facial_asymmetry": ("FLOAT", {"default": 0, "min": 0, "max": max_float_value, "step": 0.05, "display": "slider"}),
                "hair_style": (['-'] + [rand_opt] + lists['hair_style'], {"default": '-'}),
                "hair_color": (['-'] + [rand_opt] + lists['hair_color'], {"default": '-'}),
                "hair_length": (['-'] + [rand_opt] + lists['hair_length'], {"default": '-'}),
                "disheveled": ("FLOAT", {"default": 0, "min": 0, "max": max_float_value, "step": 0.05, "display": "slider"}),
                "beard": (['-'] + [rand_opt] + lists['beard'], {"default": '-'}),
                "beard_color": (['-'] + [rand_opt] + lists['beard_color'], {"default": '-'}),
                "active": ("BOOLEAN", {"default": True}),
                "load_preset": (["-- disabled --"] + preset_files, ),
                "save_preset_as": ("STRING", {"default": ""}),
                "save_preset": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "pmbc"
    CATEGORY = "AI WizArt/Portrait Master"

    def pmbc(self, **kwargs):
        params = handle_presets(self, **kwargs)

        text_in=params.get('text_in','')
        shot=params.get('shot','-')
        shot_weight=params.get('shot_weight',1)
        gender=params.get('gender','-')
        androgynous=params.get('androgynous',0)
        ugly=params.get('ugly',0)
        ordinary_face=params.get('ordinary_face',0)
        age=params.get('age',30)
        nationality_1=params.get('nationality_1','-')
        nationality_2=params.get('nationality_2','-')
        nationality_mix=params.get('nationality_mix',0.5)
        body_type=params.get('body_type','-')
        body_type_weight=params.get('body_type_weight',1)
        breast_size=params.get('breast_size','-')
        breast_size_weight=params.get('breast_size_weight',1)
        butt_size=params.get('butt_size','-')
        butt_size_weight=params.get('butt_size_weight',1)
        eyes_color=params.get('eyes_color','-')
        eyes_shape=params.get('eyes_shape','-')
        lips_color=params.get('lips_color','-')
        lips_shape=params.get('lips_shape','-')
        facial_expression=params.get('facial_expression','-')
        facial_expression_weight=params.get('facial_expression_weight',1)
        face_shape=params.get('face_shape','-')
        face_shape_weight=params.get('face_shape_weight',1)
        facial_asymmetry=params.get('facial_asymmetry',0)
        hair_style=params.get('hair_style','-')
        hair_color=params.get('hair_color','-')
        hair_length=params.get('hair_length','-')
        disheveled=params.get('disheveled',0)
        beard=params.get('beard','-')
        beard_color=params.get('beard_color','-')
        active=params.get('active',True)

        prompt = []
        if text_in: prompt.append(text_in)
        if active:
            if shot_weight > 0:
                if shot == rand_opt: prompt.append(applyWeight(random.choice(lists['shot']),shot_weight))
                elif shot != '-': prompt.append(applyWeight(shot,shot_weight))
            gender_opt = ''
            if gender == rand_opt: gender_opt = random.choice(lists['gender']) + ' '
            elif gender != '-': gender_opt = gender + ' '
            age_opt = ''
            if age == rand_opt: age_opt = random.choice(lists['age']) + '-years-old '
            elif age != '-': age_opt = f'{age}-years-old '
            androgynous_opt = applyWeight('androgynous',androgynous) + ' ' if androgynous > 0 else ''
            ugly_opt = applyWeight('ugly',ugly) + ' ' if ugly > 0 else ''
            nationality = ''
            if nationality_1 != '-' or nationality_2 != '-':
                n1 = random.choice(lists['nationality']) if nationality_1 == rand_opt else nationality_1
                n2 = random.choice(lists['nationality']) if nationality_2 == rand_opt else nationality_2
                if n1 and n2 and n1 != '-' and n2 != '-': nationality = f'[{n1}:{n2}:{str(round(nationality_mix, 2))}] '
                else: nationality = (n1 if n1 != '-' else n2) + ' '
            if androgynous_opt or ugly_opt or nationality or gender_opt or age_opt:
                t = f'({androgynous_opt}{ugly_opt}{nationality}{gender_opt}{age_opt}:1.15)'.strip()
                prompt.append(t)
            if ordinary_face > 0: prompt.append(applyWeight('ordinary face',ordinary_face))
            if body_type_weight > 0:
                if body_type == rand_opt: prompt.append(applyWeight(random.choice(lists['body_type']) + ' body',body_type_weight))
                elif body_type != '-': prompt.append(applyWeight(body_type,body_type_weight) + ' body')
            if breast_size_weight > 0:
                if breast_size == rand_opt: prompt.append(applyWeight(random.choice(lists['breast_size']) + ' breasts',breast_size_weight))
                elif breast_size != '-': prompt.append(applyWeight(breast_size + ' breasts',breast_size_weight))
            if butt_size_weight > 0:
                if butt_size == rand_opt: prompt.append(applyWeight(random.choice(lists['butt_size']) + ' butt',butt_size_weight))
                elif butt_size != '-': prompt.append(applyWeight(butt_size + ' butt',butt_size_weight))
            if eyes_color == rand_opt: prompt.append(f"({random.choice(lists['eyes_color'])} eyes:1.05)")
            elif eyes_color != '-': prompt.append(f"({eyes_color} eyes:1.05)")
            if eyes_shape == rand_opt: prompt.append(f"({random.choice(lists['eyes_shape'])}:1.05)")
            elif eyes_shape != '-': prompt.append(f"({eyes_shape}:1.05)")
            if lips_color == rand_opt: prompt.append(f"({random.choice(lists['lips_color'])}:1.05)")
            elif lips_color != '-': prompt.append(f"({lips_color}:1.05)")
            if lips_shape == rand_opt: prompt.append(f"({random.choice(lists['lips_shape'])}:1.05)")
            elif lips_shape != '-': prompt.append(f"({lips_shape}:1.05)")
            if facial_expression_weight > 0:
                if facial_expression == rand_opt: prompt.append(applyWeight(f"{random.choice(lists['face_expression'])} expression",facial_expression_weight))
                elif facial_expression != '-': prompt.append(applyWeight(f"{facial_expression} expression",facial_expression_weight))
            if face_shape_weight > 0:
                if face_shape == rand_opt: prompt.append(applyWeight(f"{random.choice(lists['face_shape'])} face-shape",face_shape_weight))
                elif face_shape != '-': prompt.append(applyWeight(f"{face_shape} face-shape",face_shape_weight))
            if facial_asymmetry > 0: prompt.append(applyWeight('facial asymmetry, face asymmetry',facial_asymmetry))
            if hair_style == rand_opt: prompt.append(f"({random.choice(lists['hair_style'])} hair style:1.05)")
            elif hair_style != '-': prompt.append(f"({hair_style} hair style:1.05)")
            if hair_color == rand_opt: prompt.append(f"({random.choice(lists['hair_color'])} hair color:1.05)")
            elif hair_color != '-': prompt.append(f"({hair_color} hair color:1.05)")
            if hair_length == rand_opt: prompt.append(f"({random.choice(lists['hair_length'])} hair length:1.05)")
            elif hair_length != '-': prompt.append(f"({hair_length} hair length:1.05)")
            if disheveled > 0: prompt.append(applyWeight('disheveled',disheveled))
            if beard == rand_opt: prompt.append(f"({random.choice(lists['beard'])}:1.05)")
            elif beard != '-': prompt.append(f"({beard}:1.05)")
            if beard_color == rand_opt: prompt.append(f"({random.choice(lists['beard_color'])} beard color:1.05)")
            elif beard_color != '-': prompt.append(f"({beard_color} beard color:1.05)")
        return (', '.join(prompt).lower(),) if prompt else ('',)

# Portrait Master Skin Details

class PortraitMasterSkinDetails:
    preset_class = "SkinDetails"

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        preset_files = get_presets(s.preset_class)
        return {
            "optional": {"text_in": ("STRING", {"forceInput": True}),"seed": ("INT", {"forceInput": False})},
            "required": {
                "natural_skin": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "bare_face": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "washed_face": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "dried_face": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "skin_details": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "skin_pores": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "dimples": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "wrinkles": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "freckles": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "moles": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "skin_imperfections": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "skin_acne": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "tanned_skin": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "eyes_details": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "iris_details": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "circular_iris": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "circular_pupil": ("FLOAT", {"default": 0,"min": 0,"max": max_float_value,"step": 0.05,"display": "slider"}),
                "active": ("BOOLEAN", {"default": True}),
                "load_preset": (["-- disabled --"] + preset_files, ),
                "save_preset_as": ("STRING", {"default": ""}),
                "save_preset": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "pmsd"
    CATEGORY = "AI WizArt/Portrait Master"

    def pmsd(self, **kwargs):
        params = handle_presets(self, **kwargs)
        text_in=params.get('text_in','')
        natural_skin=params.get('natural_skin',0)
        bare_face=params.get('bare_face',0)
        washed_face=params.get('washed_face',0)
        dried_face=params.get('dried_face',0)
        skin_details=params.get('skin_details',0)
        skin_pores=params.get('skin_pores',0)
        dimples=params.get('dimples',0)
        wrinkles=params.get('wrinkles',0)
        freckles=params.get('freckles',0)
        moles=params.get('moles',0)
        skin_imperfections=params.get('skin_imperfections',0)
        skin_acne=params.get('skin_acne',0)
        tanned_skin=params.get('tanned_skin',0)
        eyes_details=params.get('eyes_details',0)
        iris_details=params.get('iris_details',0)
        circular_iris=params.get('circular_iris',0)
        circular_pupil=params.get('circular_pupil',0)
        active=params.get('active',True)

        prompt = []
        if text_in: prompt.append(text_in)
        if active:
            if natural_skin > 0: prompt.append(applyWeight('natural skin',natural_skin))
            if bare_face > 0: prompt.append(applyWeight('bare face',bare_face))
            if washed_face > 0: prompt.append(applyWeight('washed-face',washed_face))
            if dried_face > 0: prompt.append(applyWeight('dried-face',dried_face))
            if skin_details > 0: prompt.append(applyWeight('detailed skin',skin_details))
            if skin_pores > 0: prompt.append(applyWeight('skin pores',skin_pores))
            if skin_imperfections > 0: prompt.append(applyWeight('skin imperfections',skin_imperfections))
            if skin_acne > 0: prompt.append(applyWeight('acne, skin with acne',skin_acne))
            if wrinkles > 0: prompt.append(applyWeight('wrinkles',wrinkles))
            if tanned_skin > 0: prompt.append(applyWeight('tanned skin',tanned_skin))
            if dimples > 0: prompt.append(applyWeight('dimples',dimples))
            if freckles > 0: prompt.append(applyWeight('freckles',freckles))
            if moles > 0: prompt.append(applyWeight('moles',moles))
            if eyes_details > 0: prompt.append(applyWeight('eyes details',eyes_details))
            if iris_details > 0: prompt.append(applyWeight('iris details',iris_details))
            if circular_iris > 0: prompt.append(applyWeight('circular details',circular_iris))
            if circular_pupil > 0: prompt.append(applyWeight('circular pupil',circular_pupil))
        return (', '.join(prompt).lower(),) if prompt else ('',)

# Portrait Master Style & Pose

class PortraitMasterStylePose:
    preset_class = "StylePose"

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        preset_files = get_presets(s.preset_class)
        return {
            "optional": {"text_in": ("STRING", {"forceInput": True}), "seed": ("INT", {"forceInput": False})},
            "required": {
                "model_pose": (['-'] + [rand_opt] + lists['model_pose'], {"default": '-'}),
                "clothes": (['-'] + [rand_opt] + lists['clothes'], {"default": '-'}),
                "female_lingerie": (['-'] + [rand_opt] + lists['female_lingerie'], {"default": '-'}),
                "makeup": (['-'] + [rand_opt] + lists['makeup'], {"default": '-'}),
                "light_type": (['-'] + [rand_opt] + lists['light_type'], {"default": '-'}),
                "light_direction": (['-'] + [rand_opt] + lists['light_direction'], {"default": '-'}),
                "light_weight": ("FLOAT", {"default": 1, "min": 0, "max": max_float_value, "step": 0.05, "display": "slider"}),
                "style_1": (['-'] + [rand_opt] + lists['style'], {"default": '-'}),
                "style_1_weight": ("FLOAT", {"default": 1, "min": 0, "max": max_float_value, "step": 0.05, "display": "slider"}),
                "style_2": (['-'] + [rand_opt] + lists['style'], {"default": '-'}),
                "style_2_weight": ("FLOAT", {"default": 1, "min": 0, "max": max_float_value, "step": 0.05, "display": "slider"}),
                "photorealism_improvement": ("BOOLEAN", {"default": True}),
                "active": ("BOOLEAN", {"default": True}),
                "load_preset": (["-- disabled --"] + preset_files, ),
                "save_preset_as": ("STRING", {"default": ""}),
                "save_preset": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "pmsp"
    CATEGORY = "AI WizArt/Portrait Master"

    def pmsp(self, **kwargs):
        params = handle_presets(self, **kwargs)
        text_in=params.get('text_in','')
        model_pose=params.get('model_pose','-')
        clothes=params.get('clothes','-')
        female_lingerie=params.get('female_lingerie','-')
        makeup=params.get('makeup','-')
        light_type=params.get('light_type','-')
        light_direction=params.get('light_direction','-')
        light_weight=params.get('light_weight',1)
        style_1=params.get('style_1','-')
        style_1_weight=params.get('style_1_weight',1)
        style_2=params.get('style_2','-')
        style_2_weight=params.get('style_2_weight',1)
        photorealism_improvement=params.get('photorealism_improvement',False)
        active=params.get('active',True)

        prompt = []
        if text_in: prompt.append(text_in)
        if active:
            if makeup == rand_opt: prompt.append(f"({random.choice(lists['makeup'])}:1.05)")
            elif makeup != '-': prompt.append(f"({makeup}:1.05)")
            if model_pose == rand_opt: prompt.append(f"({random.choice(lists['model_pose'])}:1.25)")
            elif model_pose != '-': prompt.append(f"({model_pose}:1.25)")
            if clothes == rand_opt: prompt.append(f"({random.choice(lists['clothes'])}:1.25)")
            elif clothes != '-': prompt.append(f"({clothes}:1.25)")
            if female_lingerie == rand_opt: prompt.append(f"({random.choice(lists['female_lingerie'])}:1.25)")
            elif female_lingerie != '-': prompt.append(f"({female_lingerie}:1.25)")
            if light_type == rand_opt: prompt.append(applyWeight(random.choice(lists['light_type']),light_weight))
            elif light_type != '-': prompt.append(applyWeight(light_type,light_weight))
            if light_direction == rand_opt: prompt.append(applyWeight(random.choice(lists['light_direction']),light_weight))
            elif light_direction != '-': prompt.append(applyWeight(light_direction,light_weight))
            if style_1 == rand_opt: prompt.append(applyWeight(random.choice(lists['style']),style_1_weight))
            elif style_1 != '-': prompt.append(applyWeight(style_1,style_1_weight))
            if style_2 == rand_opt: prompt.append(applyWeight(random.choice(lists['style']),style_2_weight))
            elif style_2 != '-': prompt.append(applyWeight(style_2,style_2_weight))
            if photorealism_improvement: prompt.append('(professional photo, balanced photo, balanced exposure:1.2)')
        return (', '.join(prompt).lower(),) if prompt else ('',)

# Portrait Master Makeup

class PortraitMasterMakeup:
    preset_class = "Makeup"

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        preset_files = get_presets(s.preset_class)
        return {
            "optional": {"text_in": ("STRING", {"forceInput": True}), "seed": ("INT", {"forceInput": False})},
            "required": {
                "makeup_style": (['-'] + [rand_opt] + lists['makeup'], {"default": '-'}),
                "makeup_color": (['-'] + [rand_opt] + lists['makeup_color'], {"default": '-'}),
                "eyeshadow": ("BOOLEAN", {"default": False}),
                "eyeliner": ("BOOLEAN", {"default": False}),
                "mascara": ("BOOLEAN", {"default": False}),
                "blush": ("BOOLEAN", {"default": False}),
                "lipstick": ("BOOLEAN", {"default": False}),
                "lip_gloss": ("BOOLEAN", {"default": False}),
                "active": ("BOOLEAN", {"default": True}),
                "load_preset": (["-- disabled --"] + preset_files, ),
                "save_preset_as": ("STRING", {"default": ""}),
                "save_preset": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "pmmk"
    CATEGORY = "AI WizArt/Portrait Master"

    def pmmk(self, **kwargs):
        params = handle_presets(self, **kwargs)
        text_in=params.get('text_in','')
        makeup_style=params.get('makeup_style','-')
        makeup_color=params.get('makeup_color','-')
        eyeshadow=params.get('eyeshadow',False)
        eyeliner=params.get('eyeliner',False)
        mascara=params.get('mascara',False)
        blush=params.get('blush',False)
        lipstick=params.get('lipstick',False)
        lip_gloss=params.get('lip_gloss',False)
        active=params.get('active',True)

        prompt = []
        if text_in: prompt.append(text_in)
        if active:
            if makeup_style == rand_opt: prompt.append(f"({random.choice(lists['makeup'])}:1.05)")
            elif makeup_style != '-': prompt.append(f"({makeup_style}:1.05)")
            if makeup_color == rand_opt: prompt.append(f"({random.choice(lists['makeup_color'])} make-up color:1.05)")
            elif makeup_color != '-': prompt.append(f"({makeup_color} make-up color:1.05)")
            if eyeshadow: prompt.append("(eyeshadow make-up:1.05)")
            if eyeliner: prompt.append("(eyeliner make-up:1.05)")
            if mascara: prompt.append("(mascara make-up:1.05)")
            if blush: prompt.append("(blush make-up:1.05)")
            if lipstick: prompt.append("(lipstick make-up:1.05)")
            if lip_gloss: prompt.append("(lip gloss make-up:1.05)")
        return (', '.join(prompt).lower(),) if prompt else ('',)

# Portrait Master Face Generator

class PortraitMasterFaceGenerator:
    preset_class = "FaceGenerator"

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        preset_files = get_presets(s.preset_class)
        return {
            "optional": {"text_in": ("STRING", {"forceInput": True}), "seed": ("INT", {"forceInput": False})},
            "required": {
                "gender": (['-'] + [rand_opt] + lists['gender'], {"default": '-'}),
                "age": (['-'] + [rand_opt] + lists['age'], {"default": '-'}),
                "nationality": (['-'] + [rand_opt] + lists['nationality'], {"default": '-'}),
                "body_type": (['-'] + [rand_opt] + lists['body_type'], {"default": '-'}),
                "eyes_color": (['-'] + [rand_opt] + lists['eyes_color'], {"default": '-'}),
                "hair_style": (['-'] + [rand_opt] + lists['hair_style'], {"default": '-'}),
                "hair_color": (['-'] + [rand_opt] + lists['hair_color'], {"default": '-'}),
                "hair_length": (['-'] + [rand_opt] + lists['hair_length'], {"default": '-'}),
                "beard": (['-'] + [rand_opt] + lists['beard'], {"default": '-'}),
                "beard_color": (['-'] + [rand_opt] + lists['beard_color'], {"default": '-'}),
                "active": ("BOOLEAN", {"default": True}),
                "load_preset": (["-- disabled --"] + preset_files, ),
                "save_preset_as": ("STRING", {"default": ""}),
                "save_preset": ("BOOLEAN", {"default": False}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "pmfg"
    CATEGORY = "AI WizArt/Portrait Master"

    def pmfg(self, **kwargs):
        params = handle_presets(self, **kwargs)
        
        text_in = params.get('text_in', '')
        gender = params.get('gender', '-')
        age = params.get('age', '-')
        nationality = params.get('nationality', '-')
        body_type = params.get('body_type', '-')
        eyes_color = params.get('eyes_color', '-')
        hair_style = params.get('hair_style', '-')
        hair_color = params.get('hair_color', '-')
        hair_length = params.get('hair_length', '-')
        beard = params.get('beard', '-')
        beard_color = params.get('beard_color', '-')
        active = params.get('active', True)

        prompt = []
        if text_in: 
            prompt.append(text_in)
        
        if active:
            # Base setup per volto frontale simmetrico
            prompt.append("front view portrait")
            prompt.append("symmetrical face")
            prompt.append("neutral expression")
            prompt.append("white background")
            prompt.append("soft diffused lighting")
            
            # Caratteristiche del personaggio
            character_parts = []
            
            # Genere
            if gender == rand_opt:
                character_parts.append(random.choice(lists['gender']).lower())
            elif gender != '-':
                character_parts.append(gender.lower())
            
            # Età
            if age == rand_opt:
                character_parts.append(f"{random.choice(lists['age'])}-years-old")
            elif age != '-':
                character_parts.append(f"{age}-years-old")
            
            # Nazionalità
            if nationality == rand_opt:
                character_parts.append(random.choice(lists['nationality']).lower())
            elif nationality != '-':
                character_parts.append(nationality.lower())
            
            # Tipo di corpo
            if body_type == rand_opt:
                character_parts.append(f"{random.choice(lists['body_type']).lower()} body")
            elif body_type != '-':
                character_parts.append(f"{body_type.lower()} body")
            
            if character_parts:
                prompt.append(" ".join(character_parts))
            
            # Colore occhi
            if eyes_color == rand_opt:
                prompt.append(f"{random.choice(lists['eyes_color']).lower()} eyes")
            elif eyes_color != '-':
                prompt.append(f"{eyes_color.lower()} eyes")
            
            # Stile capelli
            if hair_style == rand_opt:
                prompt.append(f"{random.choice(lists['hair_style']).lower()} hair style")
            elif hair_style != '-':
                prompt.append(f"{hair_style.lower()} hair style")
            
            # Colore capelli
            if hair_color == rand_opt:
                prompt.append(f"{random.choice(lists['hair_color']).lower()} hair")
            elif hair_color != '-':
                prompt.append(f"{hair_color.lower()} hair")
            
            # Lunghezza capelli
            if hair_length == rand_opt:
                prompt.append(f"{random.choice(lists['hair_length']).lower()} hair length")
            elif hair_length != '-':
                prompt.append(f"{hair_length.lower()} hair length")
            
            # Barba
            if beard == rand_opt:
                prompt.append(random.choice(lists['beard']).lower())
            elif beard != '-':
                prompt.append(beard.lower())
            
            # Colore barba
            if beard_color == rand_opt:
                prompt.append(f"{random.choice(lists['beard_color']).lower()} beard")
            elif beard_color != '-':
                prompt.append(f"{beard_color.lower()} beard")
        
        return (', '.join(prompt),) if prompt else ('',)


# Portrait Master Prompt Styler

class PortraitMasterPromptStyler:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_in": ("STRING", {"forceInput": True}),
                "style": (["descriptive", "cinematic", "illustrative", "artistic", "documentary", "fashion"], {"default": "descriptive"}),
                "add_extra_instructions": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "pm_prompt_styler"
    CATEGORY = "AI WizArt/Portrait Master"

    def pm_prompt_styler(self, text_in, style="descriptive", add_extra_instructions=True):
        tags = [t.strip() for t in text_in.split(',') if t.strip()]
        clean_tags = []
        for tag in tags:
            if '(' in tag and ')' in tag:
                content = tag.split('(')[1].split(')')[0]
                if ':' in content: content = content.split(':')[0].strip()
                clean_tags.append(content)
            else: clean_tags.append(tag)
        clean_tags = list(dict.fromkeys(clean_tags))
        style_prompts = {
            "descriptive": "A detailed photo of {subject} including the following features: {description}.",
            "cinematic": "Cinematic photo of {subject}, {description}, dramatic lighting, cinematic composition.",
            "illustrative": "Illustration of {subject}, {description}, suitable for concept art or digital illustration.",
            "artistic": "{subject} portrayed artistically with the following traits: {description}. Rich details and textures.",
            "documentary": "Documentary-style photograph of {subject} showing: {description}. Natural lighting, realistic scene.",
            "fashion": "Fashion editorial shot of {subject}, {description}, stylish pose, professional photography."
        }
        subject = "a person"
        for tag in clean_tags:
            if any(x in tag for x in ['girl', 'woman', 'female']): subject = "a woman"
            elif any(x in tag for x in ['boy', 'man', 'male']): subject = "a man"
            elif 'young' in tag: subject = f"a young {subject}"
        description = ", ".join(clean_tags)
        prompt_base = style_prompts.get(style, style_prompts['descriptive'])
        final_prompt = prompt_base.format(subject=subject, description=description)
        if add_extra_instructions: final_prompt += " Photorealistic, high resolution, dynamic lighting, intricate details."
        return (final_prompt,)

NODE_CLASS_MAPPINGS = {
    "PortraitMasterBaseCharacter": PortraitMasterBaseCharacter,
    "PortraitMasterSkinDetails": PortraitMasterSkinDetails,
    "PortraitMasterStylePose": PortraitMasterStylePose,
    "PortraitMasterMakeup": PortraitMasterMakeup,
    "PortraitMasterPromptStyler": PortraitMasterPromptStyler,
    "PortraitMasterFaceGenerator": PortraitMasterFaceGenerator,
    "PortraitMaster": PortraitMaster,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PortraitMasterBaseCharacter": "Portrait Master: Base Character",
    "PortraitMasterSkinDetails": "Portrait Master: Skin Details",
    "PortraitMasterStylePose": "Portrait Master: Style & Pose",
    "PortraitMasterMakeup": "Portrait Master: Make-up",
    "PortraitMasterPromptStyler": "Portrait Master: Prompt Styler",
    "PortraitMasterFaceGenerator": "Portrait Master: Face Generator",
    "PortraitMaster": "Portrait Master 2.9.2 (Legacy)",
}
