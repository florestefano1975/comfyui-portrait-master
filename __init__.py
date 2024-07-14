# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Version: 3.1
# https://stefanoflore.it
# https://ai-wiz.art

import os
import random
from .legacy import PortraitMaster

script_dir = os.path.dirname(__file__)

# read txt file

def pmReadTxt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        values = [line.strip() for line in lines]
        return values

# apply weight
    
def applyWeight(text, weight):
    if weight == 1:
        return text
    else:
        return f"({text}:{round(weight,2)})"

# global vars

rand_opt = 'random 🎲'

# Load lists

def load_lists():
    lists = {}
    list_names = [
        "shot", "gender", "face_shape", "face_expression", "nationality", "hair_style",
        "light_type", "light_direction", "eyes_color", "eyes_shape", "beard_color",
        "hair_color", "hair_length", "body_type", "beard", "model_pose", "style",
        "lips_shape", "lips_color", "makeup", "clothes", "age", "makeup_color"
    ]
    for name in list_names:
        list_path = os.path.join(script_dir, f"lists/{name}_list.txt")
        lists[name] = pmReadTxt(list_path)
        lists[name].sort()
    return lists

lists = load_lists()

# Portrait Master Base Character

class PortraitMasterBaseCharacter:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "optional": {
                "text_in": ("STRING", {"forceInput": True}),
                "seed": ("INT", {"forceInput": True}),
            },
            "required": {
                "shot": (['-'] + [rand_opt] + lists['shot'], {
                    "default": '-',
                }),
                "shot_weight": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "gender": (['-'] + [rand_opt] + lists['gender'], {
                    "default": '-',
                }),
                "androgynous": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "age": (['-'] + [rand_opt] + lists['age'], {
                    "default": '-',
                }),
                "nationality_1": (['-'] + [rand_opt] + lists['nationality'], {
                    "default": '-',
                }),
                "nationality_2": (['-'] + [rand_opt] + lists['nationality'], {
                    "default": '-',
                }),
                "nationality_mix": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": 1,
                    "step": 0.05,
                    "display": "slider",
                }),
                "body_type": (['-'] + [rand_opt] + lists['body_type'], {
                    "default": '-',
                }),
                "body_type_weight": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "eyes_color": (['-'] + [rand_opt] + lists['eyes_color'], {
                    "default": '-',
                }),
                "eyes_shape": (['-'] + [rand_opt] + lists['eyes_shape'], {
                    "default": '-',
                }),
                "lips_color": (['-'] + [rand_opt] + lists['lips_color'], {
                    "default": '-',
                }),
                "lips_shape": (['-'] + [rand_opt] + lists['lips_shape'], {
                    "default": '-',
                }),
                "facial_expression": (['-'] + [rand_opt] + lists['face_expression'], {
                    "default": '-',
                }),
                "facial_expression_weight": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "face_shape": (['-'] + [rand_opt] + lists['face_shape'], {
                    "default": '-',
                }),
                "face_shape_weight": ("FLOAT", {
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "facial_asymmetry": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "hair_style": (['-'] + [rand_opt] + lists['hair_style'], {
                    "default": '-',
                }),
                "hair_color": (['-'] + [rand_opt] + lists['hair_color'], {
                    "default": '-',
                }),
                "hair_length": (['-'] + [rand_opt] + lists['hair_length'], {
                    "default": '-',
                }),
                "disheveled": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "beard": (['-'] + [rand_opt] + lists['beard'], {
                    "default": '-',
                }),
                "beard_color": (['-'] + [rand_opt] + lists['beard_color'], {
                    "default": '-',
                }),
                "active": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)

    FUNCTION = "pmbc"

    CATEGORY = "AI WizArt/Portrait Master"

    def pmbc(
            self,
            text_in='',
            seed=0,
            shot='-',
            shot_weight=1,
            gender='-',
            androgynous=0,
            age=30,
            nationality_1='-',
            nationality_2='-',
            nationality_mix=0.5,
            body_type='-',
            body_type_weight=1,
            eyes_color='-',
            eyes_shape='-',
            lips_color='-',
            lips_shape='-',
            facial_expression='-',
            facial_expression_weight=1,
            face_shape='-',
            face_shape_weight=1,
            facial_asymmetry=0,
            hair_style='-',
            hair_color='-',
            hair_length='-',
            disheveled=0,
            beard='-',
            beard_color='-',
            active=True
        ):

        prompt = []

        if text_in != '':
            prompt.append(text_in)

        if active:

            if shot_weight > 0:
                if shot == rand_opt:
                    prompt.append(applyWeight(random.choice(lists['shot']),shot_weight))
                elif shot != '-':
                    prompt.append(applyWeight(shot,shot_weight))

            if gender == rand_opt:
                gender_opt = random.choice(lists['gender']) + ' '
            elif gender != '-':
                gender_opt = gender + ' '
            else:
                gender_opt = ''

            if age == rand_opt:
                age_opt = random.choice(lists['age']) + '-years-old '
            elif age != '-':
                age_opt = f'{age}-years-old '
            else:
                age_opt = ''

            if androgynous > 0:
                androgynous_opt = applyWeight('androgynous',androgynous) + ' '
            else:
                androgynous_opt = ''

            nationality = ''
            if nationality_1 != '-' or nationality_2 != '-':
                nationality_1_opt = random.choice(lists['nationality']) if nationality_1 == rand_opt else nationality_1
                nationality_2_opt = random.choice(lists['nationality']) if nationality_2 == rand_opt else nationality_2
                if nationality_1_opt and nationality_2_opt and nationality_1_opt != '-' and nationality_2_opt != '-':
                    nationality = f'[{nationality_1_opt}:{nationality_2_opt}:{str(round(nationality_mix, 2))}] '
                else:
                    nationality = nationality_1_opt + ' ' if nationality_1_opt != '-' else nationality_2_opt + ' '

            if androgynous_opt + nationality + gender_opt + age_opt != '':
                t = f'{androgynous_opt}{nationality}{gender_opt}{age_opt}'
                t = t.strip()
                prompt.append(t)

            if body_type_weight > 0:
                if body_type == rand_opt:
                    prompt.append(applyWeight(random.choice(lists['body_type']),body_type_weight))
                elif body_type != '-':
                    prompt.append(applyWeight(body_type,body_type_weight))

            if eyes_color == rand_opt:
                prompt.append('(' + random.choice(lists['eyes_color']) + ' eyes:1.05)')
            elif eyes_color != '-':
                prompt.append('(' + eyes_color + ' eyes:1.05)')

            if eyes_shape == rand_opt:
                prompt.append('(' + random.choice(lists['eyes_shape']) + ' eyes:1.05)')
            elif eyes_shape != '-':
                prompt.append('(' + eyes_shape + ' eyes:1.05)')

            if lips_color == rand_opt:
                prompt.append('(' + random.choice(lists['lips_color']) + ' lips:1.05)')
            elif lips_color != '-':
                prompt.append('(' + lips_color + ' lips:1.05)')

            if lips_shape == rand_opt:
                prompt.append('(' + random.choice(lists['lips_shape']) + ' Eye shape:1.05)')
            elif lips_shape != '-':
                prompt.append('(' + lips_shape + ' lips shape:1.05)')

            if facial_expression_weight > 0:
                if facial_expression == rand_opt:
                    prompt.append(applyWeight(random.choice(lists['face_expression']),facial_expression_weight))
                elif facial_expression != '-':
                    prompt.append(applyWeight(facial_expression,facial_expression_weight))

            if face_shape_weight > 0:
                if face_shape == rand_opt:
                    prompt.append(applyWeight(random.choice(lists['face_shape']) + ' face-shape',face_shape_weight))
                elif face_shape != '-':
                    prompt.append(applyWeight(face_shape + ' face-shape',face_shape_weight))

            if facial_asymmetry > 0:
                prompt.append(applyWeight('facial asymmetry, face asymmetry',facial_asymmetry))
            
            if hair_style == rand_opt:
                prompt.append('(' + random.choice(lists['hair_style']) + ' hair style:1.05)')
            elif hair_style != '-':
                prompt.append('(' + hair_style + ' hair style:1.05)')
            
            if hair_color == rand_opt:
                prompt.append('(' + random.choice(lists['hair_color']) + ' hair color:1.05)')
            elif hair_color != '-':
                prompt.append('(' + hair_color + ' hair color:1.05)')
            
            if hair_length == rand_opt:
                prompt.append('(' + random.choice(lists['hair_length']) + ' hair length:1.05)')
            elif hair_length != '-':
                prompt.append('(' + hair_length + ' hair length:1.05)')

            if disheveled > 0:
                prompt.append(applyWeight('disheveled',disheveled))

            if beard == rand_opt:
                prompt.append('(' + random.choice(lists['beard']) + ':1.05)"')
            elif beard != '-':
                prompt.append('(' + beard + ':1.05)"')

            if beard_color == rand_opt:
                prompt.append('(' + random.choice(lists['beard_color']) + ' beard color:1.05)"')
            elif beard_color != '-':
                prompt.append('(' + beard_color + ' beard color:1.05)"')

        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return('',)

# Portrait Master Skin Details

class PortraitMasterSkinDetails:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "optional": {
                "text_in": ("STRING", {"forceInput": True}),
                "seed": ("INT", {"forceInput": True}),
            },
            "required": {
                "natural_skin": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "bare_face": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "washed_face": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "dried_face": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "skin_details": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "skin_pores": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "dimples": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "wrinkles": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "freckles": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "moles": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "skin_imperfections": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "skin_acne": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "tanned_skin": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "eyes_details": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "iris_details": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "circular_iris": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "circular_pupil": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "active": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)

    FUNCTION = "pmsd"

    CATEGORY = "AI WizArt/Portrait Master"

    def pmsd(
            self,
            text_in='',
            seed=0,
            natural_skin=0,
            bare_face=0,
            washed_face=0,
            dried_face=0,
            skin_details=0,
            skin_pores=0,
            dimples=0,
            wrinkles=0,
            freckles=0,
            moles=0,
            skin_imperfections=0,
            skin_acne=0,
            tanned_skin=0,
            eyes_details=0,
            iris_details=0,
            circular_iris=0,
            circular_pupil=0,
            active=True
    ):

        prompt = []

        if text_in != '':
            prompt.append(text_in)

        if active:

            if natural_skin > 0:
                prompt.append(applyWeight('natural skin',natural_skin))

            if bare_face > 0:
                prompt.append(applyWeight('bare face',bare_face))

            if washed_face > 0:
                prompt.append(applyWeight('washed-face',washed_face))

            if dried_face > 0:
                prompt.append(applyWeight('dried-face',dried_face))

            if skin_details > 0:
                prompt.append(applyWeight('detailed skin',skin_details))

            if skin_pores > 0:
                prompt.append(applyWeight('skin pores',skin_pores))

            if skin_imperfections > 0:
                prompt.append(applyWeight('skin imperfections',skin_imperfections))

            if skin_acne > 0:
                prompt.append(applyWeight('acne, skin with acne',skin_acne))

            if wrinkles > 0:
                prompt.append(applyWeight('wrinkles',wrinkles))

            if tanned_skin > 0:
                prompt.append(applyWeight('tanned skin',tanned_skin))

            if dimples > 0:
                prompt.append(applyWeight('dimples',dimples))

            if freckles > 0:
                prompt.append(applyWeight('freckles',freckles))

            if moles > 0:
                prompt.append(applyWeight('moles',moles))

            if eyes_details > 0:
                prompt.append(applyWeight('eyes details',eyes_details))

            if iris_details > 0:
                prompt.append(applyWeight('iris details',iris_details))

            if circular_iris > 0:
                prompt.append(applyWeight('circular details',circular_iris))

            if circular_pupil > 0:
                prompt.append(applyWeight('circular pupil',circular_pupil))

        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return('',)

# Portrait Master Style & Pose

class PortraitMasterStylePose:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "optional": {
                "text_in": ("STRING", {"forceInput": True}),
                "seed": ("INT", {"forceInput": True}),
            },
            "required": {
                "model_pose": (['-'] + [rand_opt] + lists['model_pose'], {
                    "default": '-',
                }),
                "clothes": (['-'] + [rand_opt] + lists['clothes'], {
                    "default": '-',
                }),
                "makeup": (['-'] + [rand_opt] + lists['makeup'], {
                    "default": '-',
                }),
                "light_type": (['-'] + [rand_opt] + lists['light_type'], {
                    "default": '-',
                }),
                "light_direction": (['-'] + [rand_opt] + lists['light_direction'], {
                    "default": '-',
                }),
                "light_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "style_1": (['-'] + [rand_opt] + lists['style'], {
                    "default": '-',
                }),
                "style_1_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "style_2": (['-'] + [rand_opt] + lists['style'], {
                    "default": '-',
                }),
                "style_2_weight": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "photorealism_improvement": ("BOOLEAN", {"default": True}),
                "active": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)

    FUNCTION = "pmsp"

    CATEGORY = "AI WizArt/Portrait Master"

    def pmsp(
            self,
            text_in='',
            seed=0,
            model_pose='-',
            clothes='-',
            makeup='-',
            light_type='-',
            light_direction='-',
            light_weight=1,
            style_1='-',
            style_1_weight=1,
            style_2='-',
            style_2_weight=1,
            photorealism_improvement=False,
            active=True
    ):
        
        prompt = []

        if text_in != '':
            prompt.append(text_in)

        if active:

            if makeup == rand_opt:
                prompt.append('(' + random.choice(lists['makeup']) + ':1.05)')
            elif makeup != '-':
                prompt.append(f"({makeup}:1.05)")

            if model_pose == rand_opt:
                prompt.append('(' + random.choice(lists['model_pose']) + ':1.25)')
            elif model_pose != '-':
                prompt.append(f"({model_pose}:1.25)")

            if clothes == rand_opt:
                prompt.append('(' + random.choice(lists['clothes']) + ':1.25)')
            elif clothes != '-':
                prompt.append(f"({clothes}:1.25)")

            if light_type == rand_opt:
                prompt.append(applyWeight(random.choice(lists['light_type']),light_weight))
            elif light_type != '-':
                prompt.append(applyWeight(light_type,light_weight))

            if light_direction == rand_opt:
                prompt.append(applyWeight(random.choice(lists['light_direction']),light_weight))
            elif light_direction != '-':
                prompt.append(applyWeight(light_direction,light_weight))

            if style_1 == rand_opt:
                prompt.append(applyWeight(random.choice(lists['style']),style_1_weight))
            elif style_1 != '-':
                prompt.append(applyWeight(style_1,style_1_weight))

            if style_2 == rand_opt:
                prompt.append(applyWeight(random.choice(lists['style']),style_2_weight))
            elif style_2 != '-':
                prompt.append(applyWeight(style_2,style_2_weight))

            if photorealism_improvement:
                prompt.append('(professional photo, balanced photo, balanced exposure:1.2)')

        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return('',)

# Portrait Master Makeup

class PortraitMasterMakeup:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 2
        return {
            "optional": {
                "text_in": ("STRING", {"forceInput": True}),
                "seed": ("INT", {"forceInput": True}),
            },
            "required": {
                "makeup_style": (['-'] + [rand_opt] + lists['makeup'], {
                    "default": '-',
                }),
                "makeup_color": (['-'] + [rand_opt] + lists['makeup_color'], {
                    "default": '-',
                }),
                "eyeshadow": ("BOOLEAN", {"default": False}),
                "eyeliner": ("BOOLEAN", {"default": False}),
                "mascara": ("BOOLEAN", {"default": False}),
                "blush": ("BOOLEAN", {"default": False}),
                "lipstick": ("BOOLEAN", {"default": False}),
                "lip_gloss": ("BOOLEAN", {"default": False}),
                "active": ("BOOLEAN", {"default": True}),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)

    FUNCTION = "pmmk"

    CATEGORY = "AI WizArt/Portrait Master"

    def pmmk(
            self,
            text_in='',
            seed=0,
            makeup_style='-',
            makeup_color='-',
            eyeshadow=False,
            eyeliner=False,
            mascara=False,
            blush=False,
            lipstick=False,
            lip_gloss=False,
            active=True,
    ):
        
        prompt = []

        if text_in != '':
            prompt.append(text_in)

        if active:

            if makeup_style == rand_opt:
                prompt.append('(' + random.choice(lists['makeup']) + ':1.05)')
            elif makeup_style != '-':
                prompt.append(f"({makeup_style}:1.05)")

            if makeup_color == rand_opt:
                prompt.append('(' + random.choice(lists['makeup_color']) + ' make-up color:1.05)')
            elif makeup_color != '-':
                prompt.append(f"({makeup_color} make-up color:1.05)")

            if eyeshadow: prompt.append("(eyeshadow make-up:1.05)")
            if eyeliner: prompt.append("(eyeliner make-up:1.05)")
            if mascara: prompt.append("(mascara make-up:1.05)")
            if blush: prompt.append("(blush make-up:1.05)")
            if lipstick: prompt.append("(lipstick make-up:1.05)")
            if lip_gloss: prompt.append("(lip gloss make-up:1.05)")

        if len(prompt) > 0:
            prompt = ', '.join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return('',)

NODE_CLASS_MAPPINGS = {
    "PortraitMasterBaseCharacter": PortraitMasterBaseCharacter,
    "PortraitMasterSkinDetails": PortraitMasterSkinDetails,
    "PortraitMasterStylePose": PortraitMasterStylePose,
    "PortraitMasterMakeup": PortraitMasterMakeup,
    "PortraitMaster": PortraitMaster
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PortraitMasterBaseCharacter": "Portrait Master: Base Character",
    "PortraitMasterSkinDetails": "Portrait Master: Skin Details",
    "PortraitMasterStylePose": "Portrait Master: Style & Pose",
    "PortraitMasterMakeup": "Portrait Master: Make-up",
    "PortraitMaster": "Portrait Master 2.9.2 (Legacy)"
}
