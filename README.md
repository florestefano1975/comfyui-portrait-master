# ComfyUI Portrait Master

This node was designed to help AI image creators to generate prompts for human portraits.

![ComfyUI Portrait Master Node](/screenshot/portrait-master-node.png)

## Install

To install comfyui-portrait-master in addition to an existing installation of ComfyUI, you can follow the following steps:

1. open the terminal on the ComfyUI installation folder
2. digit: `cd custom_nodes`
3. digit: `git clone https://github.com/florestefano1975/comfyui-portrait-master`
4. restart ComfyUI

We recommend the use of [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) to install the additional custom nodes needed for the workflow.

## Update

To install comfyui-portrait-master in addition to an existing installation of ComfyUI, you can follow the following steps:

1. open the terminal on the ComfyUI installation folder
2. digit: `cd custom_nodes`
3. digit: `cd comfyui-portrait-master`
4. digit: `git pull`
5. restart ComfyUI

## Available Options

- **shot**: sets the shot type
- **shot_weight**: coefficient (weight) of the shot type
- **gender**: sets the character's gender
- **nationality_1**: sets first ethnicity
- **nationality_2**: sets second ethnicity
- **nationality_mix**: controls the mix between nationality_1 and nationality_2, according to the syntax [nationality_1: nationality_2: nationality_mix]. This syntax is not natively recognized by ComfyUI; we therefore recommend the use of [comfyui-prompt-control](https://github.com/asagi4/comfyui-prompt-control). _This feature is still being tested_
- **eyes_color**: set the eyes color
- **hair_color**: set the hair color
- **facial_expression**: sets the character's expression
- **facial_expression_weight**: coefficient (weight) of the expression
- **face_shape**: sets the character's face shape
- **face_shape_weight**: coefficient (weight) of the face shape
- **facial_asymmetry**: coefficient (weight) to set the asymmetry of the face
- **hairs_style**: hairstyle selector
- **disheveled**: coefficient (weight) of the disheveled effect
- **age**: the age of the subject portrayed
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
- **prompt_start**: portion of the prompt that is inserted at the beginning
- **prompt_additional**: portion of the prompt that is inserted at an intermediate point
- **prompt_end**: portion of the prompt that is inserted at the end
- **negative_prompt**: the negative prompt has been integrated into the node to be adequately controlled depending on the settings

Parameters with null value (-) or set to 0.00 are not included in the prompt generated.

The node generates two output string, postive and negative prompt.

## Customizations

The _lists_ subfolder contains the .txt files that generate the lists for some node options. You can open files and customize voices.

## Practical advice

Using high values for the skin and eye detail control parameters may override the setting for the chosen shot. In this case it is advisable to reduce the parameter values for the skin and eyes, or insert in the negative prompt (closeup, close up, close-up:1.5), modifying the weight as needed.

For total control of the pose, use the ControlNet nodes integrated into the workflow, setting the _shot_ parameter to null (-).

## Workflow

The [_portrait-master-controlnet-workflow.json_](/workflow/portrait-master-controlnet-workflow.json) file contains the workflow designed to work properly with Portrait Master.

An upscaler and ControlNet have been integrated to manage the pose of the characters. I inserted 2 switches to disable the upscaler and control if necessary. The coloring of the nodes will help you understand how the switches affect the workflow.

For the correct functioning of ControlNet with SDXL checkpoints, download the _control-lora-openposeXL2-rank256.safetensors_ file from [this link](https://huggingface.co/thibaud/controlnet-openpose-sdxl-1.0/blob/main/control-lora-openposeXL2-rank256.safetensors) and copy it into the _./models/controlnet/_ folder of ComfyUI.

There are some files that can be used with ControlNet in the Portrait Master _openpose_ folder. To generate other poses use the free portal https://openposeai.com/

![Workflow](/screenshot/portrait-master-workflow.png)

The [_portrait-master-controlnet2x-workflow.json_](/workflow/portrait-master-controlnet2x-workflowjson) file contains a dual ControlNet workflow to simultaneously manage the character's pose and hands. There are two switches to individually enable and disable the two blocks of nodes.

![Workflow](/screenshot/portrait-master-workflow-controlnet-2x.png)

## Workflow performances

The workflow is designed to obtain the right balance between quality and generative performance. You can change the settings of the two KSamplers to adapt them to your needs.

Tested on **Google Colab**, the workflow generates a high-resolution image in **60 seconds with V100 GPU** and in **30 seconds with A100 GPU**.

## Examples

In the future, several example images in PNG format will be uploaded to the examples folder, which can be uploaded to ComfyUI to use their settings.

![Example image](/examples/comfyui-portrait-master-example-001.png)

## SDXL Turbo

ComfyUI Portrait Master also works correctly with SDXL Turbo.

https://www.youtube.com/watch?v=9UbtfEH_iSk

## Notes

When the generation of an image is started in the console you can read the complete prompt created by the node.

The effectiveness of the parameters depends on the quality of the checkpoint used.

For advanced photorealism we recommend [FormulaXL 2.0](https://civitai.com/models/129922?modelVersionId=160525).
