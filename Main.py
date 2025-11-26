from diffsynth.pipelines.qwen_image import QwenImagePipeline, ModelConfig
import torch

# Initialize the pipeline
pipe = QwenImagePipeline.from_pretrained(
    torch_dtype=torch.bfloat16,
    device="cuda",
    model_configs=[
        ModelConfig(
            model_id="Qwen/Qwen-Image-Edit",
            origin_file_pattern="transformer/diffusion_pytorch_model*.safetensors"
        ),
        ModelConfig(
            model_id="Qwen/Qwen-Image",
            origin_file_pattern="text_encoder/model*.safetensors"
        ),
        ModelConfig(
            model_id="Qwen/Qwen-Image",
            origin_file_pattern="vae/diffusion_pytorch_model.safetensors"
        ),
    ],
    processor_config=ModelConfig(
        model_id="Qwen/Qwen-Image-Edit",
        origin_file_pattern="processor/"
    ),
)

# Load the Eigen-Banana-Qwen-Image-Edit LoRA
pipe.load_lora(pipe.dit, "eigen-ai-labs/eigen-banana-qwen-image-edit/eigen-banana-qwen-image-edit-fp16-lora.safetensors")

def start() =

    print("""
    Funkciók:

    (1)Szövegfelismerés
    (2)Felismert szöveg körbevágása
    (3)Szöveg képre illesztése
    (4)Háttér megváltoztatása
    (5)Fényerő megváltoztatása
    (6)Kiválasztott tárgy felismerése és körbevágása

    """)

    print("Kérem válassza ki a kívánt funkciót (1-6): ")















## Generate an initial image
#prompt = "A beautiful portrait, underwater girl, blue dress flowing, hair drifting, light penetrating, bubbles surrounding, serene face, exquisite details, dreamy and aesthetic."
#input_image = pipe(
#    prompt=prompt,
#    seed=0,
#    num_inference_steps=40,
#    height=1328,
#    width=1024
#)
#input_image.save("original.jpg")
#
## Edit the image
#edit_prompt = "Change the dress to pink"
#edited_image = pipe(
#    edit_prompt,
#    edit_image=input_image,
#    seed=1,
#    num_inference_steps=40,
#    height=1328,
#    width=1024,
#    edit_image_auto_resize=True
#)
#edited_image.save("edited.jpg")
