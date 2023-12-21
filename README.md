# ComfyUI Portrait Master

This node was designed to help AI image creators to generate prompts for human portraits.

![ComfyUI Portrait Master Node](/screenshot/portrait-master-node-2.3.png)

## Install

To install comfyui-portrait-master:

1. open the terminal on the ComfyUI installation folder
2. digit: `cd custom_nodes`
3. digit: `git clone https://github.com/florestefano1975/comfyui-portrait-master`
4. restart ComfyUI

We recommend the use of [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) to install the additional custom nodes needed for the workflow.

## Update

To update comfyui-portrait-master:

1. open the terminal on the ComfyUI installation folder
2. digit: `cd custom_nodes`
3. digit: `cd comfyui-portrait-master`
4. digit: `git pull`
5. restart ComfyUI

**Warning: update command overwrites files modified and customized by users.**

## Available Options

- **shot**: sets the shot type
- **shot_weight**: coefficient (weight) of the shot type
- **gender**: sets the character's gender
- **androgynous**: coefficient (weight) to change the genetic appearance of the character
- **nationality_1**: sets first ethnicity
- **nationality_2**: sets second ethnicity
- **nationality_mix**: controls the mix between nationality_1 and nationality_2, according to the syntax [nationality_1: nationality_2: nationality_mix]. This syntax is not natively recognized by ComfyUI; we therefore recommend the use of [comfyui-prompt-control](https://github.com/asagi4/comfyui-prompt-control). _This feature is still being tested_
- **eyes_color**: set the eyes color
- **hair_color**: set the hair color
- **facial_expression** / **facial_expression_weight**: apply and adjust character's expression
- **face_shape** / **face_shape_weight**: apply and adjust the face shape
- **facial_asymmetry**: coefficient (weight) to set the asymmetry of the face
- **hairs_style**: hairstyle selector
- **disheveled**: coefficient (weight) of the disheveled effect
- **age**: the age of the subject portrayed
- **natural_skin**: coefficient (weight) for control the natural aspect of the skin
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
- **style_1** / **style_1_weight**: apply and adjust the first style
- **style_1** / **style_1_weight**: apply and adjust the second style

Parameters with null value (-) or set to 0.00 would be not included in the prompt generated.

The node generates two output string, postive and negative prompt.

## Customizations

The _lists_ subfolder contains the .txt files that generate the lists for some node options. You can open files and customize voices.

## Workflow

The [_portrait-master-controlnet2x-workflow.json_](/workflow/portrait-master-controlnet2x-workflow.json) file contains the workflow designed to work properly with Portrait Master.

An upscaler and 2 ControlNet have been integrated to manage the pose of the characters. I inserted 3 switches to disable the upscaler and control if necessary. The coloring of the nodes will help you understand how the switches affect the workflow.

For the correct functioning of ControlNet with SDXL checkpoints, download this files:

- [_control-lora-openposeXL2-rank256.safetensors_](https://huggingface.co/thibaud/controlnet-openpose-sdxl-1.0/blob/main/control-lora-openposeXL2-rank256.safetensors)
- [sai_xl_depth_256lora.safetensors](https://huggingface.co/lllyasviel/sd_control_collection/blob/main/sai_xl_depth_256lora.safetensors)

and copy it into the _./models/controlnet/_ folder of ComfyUI. Other similar files for ControlNet are available at [this link](https://huggingface.co/lllyasviel/sd_control_collection/tree/main).

There are some files that can be used with ControlNet in the Portrait Master _openpose_ folder. To generate other poses use the free portal https://openposeai.com/

![Workflow](/screenshot/portrait-master-workflow-2.3.png)

There are some sample files in the _openpose_ folder for use with ControlNet nodes.

## Workflow performances

The workflow is designed to obtain the right balance between quality and generative performance. You can change the settings of the two KSamplers to adapt them to your needs.

Tested on **Google Colab**, the workflow generates a high-resolution image in **60 seconds with V100 GPU** and in **30 seconds with A100 GPU**.

## Model Pose Library

The _model_pose_ option allows you to use a list of default poses. You need to disable ControlNet in this case and adjust framing with the _shot_ option.

![Model Pose Library](/screenshot/portrait-master-pose-library-2.2b.jpg)

## Practical advice

Using high values for the skin and eye detail control parameters may override the setting for the chosen shot. In this case it is advisable to reduce the parameter values for the skin and eyes, or insert in the negative prompt (closeup, close up, close-up:1.5), modifying the weight as needed.

For total control of the pose, use the ControlNet nodes integrated into the workflow, setting the _shot_ parameter to null (-).

## Optimal use of prompt fields

- **prompt_start**: specify the type of image you want, for example _realistic_.
- **prompt_additional**: its content is inserted between promot_start and the part of the prompt automatically generated by the node; specify clothing and other specific characteristics of the character; possibly also the setting or background.
- **prompt_end**: in this field enter other requests to the AI, but taking into account that they are minor compared to the rest of the instructions; for example, you can move the background description or environment here. This field is not required, so you can ignore it.
- **negative_prompt**: it works as usual, it allows you to declare what you don't want in the image.

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
