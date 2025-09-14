# ComfyUI Portrait Master

This nodes was designed to help AI image creators to generate prompts for human portraits.

## Last Updates

### Version 3.5.0

- New node: **Face Generator**
- **Portrait Master Base Character**: added breast and butt options

### Version 3.4.0

- **New Preset System**: All main nodes now feature a system to save, load, and manage your favorite settings.
- The node has been divided into **five** separate modules: **Base Character**, **Skin Details**, **Style & Pose**, **Make-up**, **Prompt Styler**.
- New node: __Prompt Styler__. This node removes the declarative weights typical of the SD1.5 and SDXL models to adapt the prompt with a conversational style, more suitable for modern checkpoints such as Flux, Sana, Hidream.
- Improved code and performance.

## Donations and marketplace

**_If this project is useful to you and you like it, please consider a small donation to the author_**

➡️ https://ko-fi.com/stefanoflore75

## Overview of the custom node

![ComfyUI Portrait Master Node](/screenshot/overview.png)

## Install from ComfyUI Manager

- Type _florestefano1975_ on the search bar of [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager).
- Click the install button.

## Manual installation and update instructions

### Install

To install comfyui-portrait-master:

1. open the terminal on the ComfyUI `custom_nodes` folder
2. digit: `git clone https://github.com/florestefano1975/comfyui-portrait-master`
3. restart ComfyUI

### Update

To update comfyui-portrait-master:

1. open the terminal on the ComfyUI `comfyui-portrait-master` folder
2. digit: `git pull`
3. restart ComfyUI

**Warning: update command overwrites files modified and customized by users.**

## Presets (New in v3.4.0)

All main nodes (Base Character, Skin Details, Style & Pose, Make-up) now include a preset system to easily save and load your favorite configurations.

### How to Save a Preset

1.  Set up all the sliders and options on a node to your liking.
2.  Go to the `--- PRESETS ---` section at the bottom of the node.
3.  In the `save_preset_as` text field, type a name for your preset (e.g., "Cyberpunk Hero" or "Vintage Look").
4.  Toggle the `save_preset` switch to `True`.
5.  Queue the prompt. Your current settings will be saved as a `.json` file.
6.  After saving, you can turn the `save_preset` switch back to `False`.

### How to Load a Preset

1.  Use the `load_preset` dropdown menu. It will automatically list all the presets you have saved for that specific node.
2.  Select the preset you want to use.
3.  Queue the prompt. The node will ignore the settings on the interface and use the values from your selected preset file instead.

### Preset File Location

Your presets are saved in the `comfyui-portrait-master/presets/` directory. Each node has its own sub-directory (e.g., `presets/BaseCharacter/`, `presets/SkinDetails/`), so presets for different nodes are kept separate.

## Available Options

- **shot**: sets the shot type
- **shot_weight**: coefficient (weight) of the shot type
- **gender**: sets the character's gender
- **androgynous**: coefficient (weight) to change the genetic appearance of the character
- **age**: the age of the subject portrayed
- **nationality_1**: sets first ethnicity
- **nationality_2**: sets second ethnicity
- **nationality_mix**: controls the mix between nationality_1 and nationality_2, according to the syntax [nationality_1: nationality_2: nationality_mix]. This syntax is not natively recognized by ComfyUI; we therefore recommend the use of [comfyui-prompt-control](https://github.com/asagi4/comfyui-prompt-control). _This feature is still being tested_.
- **body_type**: set the type of the body
- **body_type_weight**: coefficient (weight) of the body type
- **model_pose**: select the pose from the list
- **eyes_color**: set the eyes color
- **eyes_shape**: set the eyes shape
- **lips_color**: set the lips color
- **lips_shape**: set the lips shape
- **makeup**: set the makeup
- **clothes**: set the clothes
- **facial_expression** / **facial_expression_weight**: apply and adjust character's expression
- **face_shape** / **face_shape_weight**: apply and adjust the face shape
- **facial_asymmetry**: coefficient (weight) to set the asymmetry of the face
- **hair_color**: set the hair color
- **hairs_style**: hairstyle selector
- **hairs_length**: hair length selector
- **disheveled**: coefficient (weight) of the disheveled effect
- **natural_skin**: coefficient (weight) for control the natural aspect of the skin
- **bare_face**: coefficient (weight) for control bare face level
- **washed_face**: coefficient (weight) for control washed face level
- **dried_face**: coefficient (weight) for control dried face level
- **skin_details**: coefficient (weight) of the skin detail
- **skin_pores**: coefficient (weight) of the skin pores
- **dimples**: coefficient (weight) for controlling facial dimples
- **freckles**: coefficient (weight) of the freckles
- **moles**: coefficient (weight) for the presence of moles on the skin
- **skin_imperfections**: coefficient (weight) to introduce skin imperfections
- **eyes_details**: coefficient (weight) for the general detail of the eyes
- **iris_details**: coefficient (weight) for the iris detail
- **circular_iris**: coefficient (weight) to increase or force the circular shape of the iris
- **circular_pupil**: coefficient (weight) to increase or force the circular shape of the pupil
- **light_type**: set global illumination
- **light_direction**: set the direction of the light. _This feature is still being tested_
- **photorealism_improvement**: experimental option to improve photorealism and the final result
- **style_1** / **style_1_weight**: apply and adjust the first style
- **style_1** / **style_1_weight**: apply and adjust the second style

Parameters with null value (-) would be not included in the prompt generated.

To enable the casual generation options, connect a random seed generator to the nodes.

The nodes generates output string.

## Model Pose Library

The _model_pose_ option allows you to use a list of default poses. You need to disable ControlNet, if in use,  in this case and adjust framing with the _shot_ option.

![Model Pose Library](/screenshot/legacy/portrait-master-pose-library-2.2b.jpg)

## Practical advice

Using high values for the skin and eye detail control parameters may override the setting for the chosen shot. In this case it is advisable to reduce the parameter values for the skin and eyes, or insert in the negative prompt (closeup, close up, close-up:1.5), modifying the weight as needed.

## Notes

The effectiveness of the parameters depends on the quality of the checkpoint used.

For advanced photorealism we recommend [FormulaXL 2.0](https://civitai.com/models/129922?modelVersionId=160525).

Portrait Master is compatible with [Prompt Composer](https://github.com/florestefano1975/comfyui-prompt-composer/).

[Portrait Master 2.9.2 (legacy) documentation](/PORTRAIT_MASTER_2.9.2.md)

## Other projects

- [ComfyUI Prompt Composer](https://github.com/florestefano1975/comfyui-prompt-composer/)
- [ComfyUI HiDiffusion](https://github.com/florestefano1975/ComfyUI-HiDiffusion/)
