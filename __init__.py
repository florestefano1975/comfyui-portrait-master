# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Version: 2.1
# https://stefanoflore.it
# https://ai-wiz.art

import os

script_dir = os.path.dirname(__file__)

# read txt file

def pmReadTxt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        values = [line.strip() for line in lines]
        return values

# setup vars

shot_list = pmReadTxt(os.path.join(script_dir, "lists/shot_list.txt"))
shot_list.sort()
shot_list = ['-'] + shot_list

gender_list = pmReadTxt(os.path.join(script_dir, "lists/gender_list.txt"))
gender_list.sort()
gender_list = ['-'] + gender_list

face_shape_list = pmReadTxt(os.path.join(script_dir, "lists/face_shape_list.txt"))
face_shape_list.sort()
face_shape_list = ['-'] + face_shape_list

facial_expressions_list = pmReadTxt(os.path.join(script_dir, "lists/face_expression_list.txt"))
facial_expressions_list.sort()
facial_expressions_list = ['-'] + facial_expressions_list

nationality_list = pmReadTxt(os.path.join(script_dir, "lists/nationality_list.txt"))
nationality_list.sort()
nationality_list = ['-'] + nationality_list

hair_style_list = pmReadTxt(os.path.join(script_dir, "lists/hair_style_list.txt"))
hair_style_list.sort()
hair_style_list = ['-'] + hair_style_list

light_type_list = pmReadTxt(os.path.join(script_dir, "lists/light_type_list.txt"))
light_type_list.sort()
light_type_list = ['-'] + light_type_list

light_direction_list = pmReadTxt(os.path.join(script_dir, "lists/light_direction_list.txt"))
light_direction_list.sort()
light_direction_list = ['-'] + light_direction_list

eyes_color_list = pmReadTxt(os.path.join(script_dir, "lists/eyes_color_list.txt"))
eyes_color_list.sort()
eyes_color_list = ['-'] + eyes_color_list

hair_color_list = pmReadTxt(os.path.join(script_dir, "lists/hair_color_list.txt"))
hair_color_list.sort()
hair_color_list = ['-'] + hair_color_list

body_type_list = pmReadTxt(os.path.join(script_dir, "lists/body_type_list.txt"))
body_type_list.sort()
body_type_list = ['-'] + body_type_list

beard_list = pmReadTxt(os.path.join(script_dir, "lists/beard_list.txt"))
beard_list.sort()
beard_list = ['-'] + beard_list

class PortraitMaster:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 1.95
        return {
            "required": {
                "shot": (shot_list, {
                    "default": shot_list[0],
                }),
                "shot_weight": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "gender": (gender_list, {
                    "default": gender_list[0],
                }),
                "age": ("INT", {
                    "default": 30,
                    "min": 18,
                    "max": 90,
                    "step": 1,
                    "display": "slider",
                }),
                "nationality_1": (nationality_list, {
                    "default": nationality_list[0],
                }),
                "nationality_2": (nationality_list, {
                    "default": nationality_list[0],
                }),
                "nationality_mix": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": 1,
                    "step": 0.05,
                    "display": "slider",
                }),
                "body_type": (body_type_list, {
                    "default": body_type_list[0],
                }),
                "body_type_weight": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "eyes_color": (eyes_color_list, {
                    "default": eyes_color_list[0],
                }),
                "facial_expression": (facial_expressions_list, {
                    "default": facial_expressions_list[0],
                }),
                "facial_expression_weight": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "face_shape": (face_shape_list, {
                    "default": face_shape_list[0],
                }),
                "face_shape_weight": ("FLOAT", {
                    "default": 0,
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
                "hair_style": (hair_style_list, {
                    "default": hair_style_list[0],
                }),
                "hair_color": (hair_color_list, {
                    "default": hair_color_list[0],
                }),
                "disheveled": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "beard": (beard_list, {
                    "default": beard_list[0],
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
                "light_type": (light_type_list, {
                    "default": light_type_list[0],
                }),
                "light_direction": (light_direction_list, {
                    "default": light_direction_list[0],
                }),
                "light_weight": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "photorealism_improvement": (["enable", "disable"],),
                "prompt_start": ("STRING", {
                    "multiline": True,
                    "default": "raw photo, (realistic:1.5)"
                }),
                "prompt_additional": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "prompt_end": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "negative_prompt": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            }
        }

    RETURN_TYPES = ("STRING","STRING",)
    RETURN_NAMES = ("positive", "negative",)

    FUNCTION = "pm"

    CATEGORY = "AI WizArt"

    def pm(self, shot="-", shot_weight=1, gender="-", body_type="-", body_type_weight=0, eyes_color="-", facial_expression="-", facial_expression_weight=0, face_shape="-", face_shape_weight=0, nationality_1="-", nationality_2="-", nationality_mix=0.5, age=30, hair_style="-", hair_color="-", disheveled=0, dimples=0, freckles=0, skin_pores=0, skin_details=0, moles=0, skin_imperfections=0, wrinkles=0, tanned_skin=0, eyes_details=1, iris_details=1, circular_iris=1, circular_pupil=1, facial_asymmetry=0, prompt_additional="", prompt_start="", prompt_end="", light_type="-", light_direction="-", light_weight=0, negative_prompt="", photorealism_improvement="disable", beard="-"):

        prompt = []

        if gender == "-":
            gender = ""
        else:
            gender = " " + gender + " "

        if nationality_1 != '-' and nationality_2 != '-':
            nationality = f"[{nationality_1}:{nationality_2}:{round(nationality_mix, 2)}]"
        elif nationality_1 != '-':
            nationality = nationality_1 + " "
        elif nationality_2 != '-':
            nationality = nationality_2 + " "
        else:
            nationality = ""

        if prompt_start != "":
            prompt.append(f"{prompt_start}")

        if shot != "-" and shot_weight > 0:
            prompt.append(f"({shot}:{round(shot_weight, 2)})")

        prompt.append(f"({nationality}{gender}{round(age)}-years-old:1.5)")

        if body_type != "-" and body_type_weight > 0:
            prompt.append(f"({body_type}, {body_type} body:{round(body_type_weight, 2)})")

        if eyes_color != "-":
            prompt.append(f"({eyes_color} eyes:1.25)")

        if facial_expression != "-" and facial_expression_weight > 0:
            prompt.append(f"({facial_expression}, {facial_expression} expression:{round(facial_expression_weight, 2)})")

        if face_shape != "-" and face_shape_weight > 0:
            prompt.append(f"({face_shape} shape face:{round(face_shape_weight, 2)})")

        if hair_style != "-":
            prompt.append(f"({hair_style} hairstyle:1.25)")

        if hair_color != "-":
            prompt.append(f"({hair_color} hair:1.25)")

        if beard != "-":
            prompt.append(f"({beard}:1.15)")

        if disheveled != "-" and disheveled > 0:
            prompt.append(f"(disheveled:{round(disheveled, 2)})")

        if prompt_additional != "":
            prompt.append(f"{prompt_additional}")

        if skin_details > 0:
            prompt.append(f"(skin details, skin texture:{round(skin_details, 2)})")

        if skin_pores > 0:
            prompt.append(f"(skin pores:{round(skin_pores, 2)})")

        if skin_imperfections > 0:
            prompt.append(f"(skin imperfections:{round(skin_imperfections, 2)})")

        if wrinkles > 0:
            prompt.append(f"(skin imperfections:{round(wrinkles, 2)})")

        if tanned_skin > 0:
            prompt.append(f"(tanned skin:{round(tanned_skin, 2)})")

        if dimples > 0:
            prompt.append(f"(dimples:{round(dimples, 2)})")

        if freckles > 0:
            prompt.append(f"(freckles:{round(freckles, 2)})")

        if moles > 0:
            prompt.append(f"(skin pores:{round(moles, 2)})")

        if eyes_details > 0:
            prompt.append(f"(eyes details:{round(eyes_details, 2)})")

        if iris_details > 0:
            prompt.append(f"(iris details:{round(iris_details, 2)})")

        if circular_iris > 0:
            prompt.append(f"(circular iris:{round(circular_iris, 2)})")

        if circular_pupil > 0:
            prompt.append(f"(circular pupil:{round(circular_pupil, 2)})")

        if facial_asymmetry > 0:
            prompt.append(f"(facial asymmetry, face asymmetry:{round(facial_asymmetry, 2)})")

        if light_type != '-' and light_weight > 0:
            if light_direction != '-':
                prompt.append(f"({light_type} {light_direction}:{round(light_weight, 2)})")
            else:
                prompt.append(f"({light_type}:{round(light_weight, 2)})")

        if prompt_end != "":
            prompt.append(f"{prompt_end}")

        prompt = ", ".join(prompt)
        prompt = prompt.lower()

        if photorealism_improvement == "enable":
            prompt = prompt + ", (detailed, professional photo, perfect exposition:1.25), (film grain:1.5)"

        if photorealism_improvement == "enable":
            negative_prompt = negative_prompt + ", (shinny skin, reflections on the skin, skin reflections:1.5)"

        print("Portrait Master as generate the prompt:")
        print(prompt)

        return (prompt,negative_prompt,)
    
NODE_CLASS_MAPPINGS = {
    "PortraitMaster": PortraitMaster
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PortraitMaster": "Portrait Master by AI Wiz Art (Stefano Flore) v.2.0"
}
