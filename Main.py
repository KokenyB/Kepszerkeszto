#from diffsynth.pipelines.qwen_image import QwenImagePipeline, ModelConfig
#import torch
import tkinter as tk
#
## Initialize the pipeline
#pipe = QwenImagePipeline.from_pretrained(
#    torch_dtype=torch.bfloat16,
#    device="cuda",
#    model_configs=[
#        ModelConfig(
#            model_id="Qwen/Qwen-Image-Edit",
#            origin_file_pattern="transformer/diffusion_pytorch_model*.safetensors"
#        ),
#        ModelConfig(
#            model_id="Qwen/Qwen-Image",
#            origin_file_pattern="text_encoder/model*.safetensors"
#        ),
#        ModelConfig(
#            model_id="Qwen/Qwen-Image",
#            origin_file_pattern="vae/diffusion_pytorch_model.safetensors"
#        ),
#    ],
#    processor_config=ModelConfig(
#        model_id="Qwen/Qwen-Image-Edit",
#        origin_file_pattern="processor/"
#    ),
#)
#
## Load the Eigen-Banana-Qwen-Image-Edit LoRA
#pipe.load_lora(pipe.dit, "eigen-ai-labs/eigen-banana-qwen-image-edit/eigen-banana-qwen-image-edit-fp16-lora.safetensors")
#
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

app = tk.Tk()
app.geometry("1200x600")
app.title("Képszerkesztő Alkalmazás")

app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=4)
app.grid_rowconfigure(2, weight=1)
app.grid_rowconfigure(3, weight=3)

bg0 = tk.Frame(app, bg="#FAF2D7")
bg0.grid(row=0, column=0, sticky="nsew")
bg0 = tk.Frame(app, bg="#FAF2D7")
bg0.grid(row=0, column=1, sticky="nsew")
bg1 = tk.Frame(app, bg="#F5EAC6")
bg1.grid(row=0, column=2, sticky="nsew")

bg0 = tk.Frame(app, bg="#FAF2D7")
bg0.grid(row=1, column=0, sticky="nsew")
bg0 = tk.Frame(app, bg="#FAF2D7")
bg0.grid(row=1, column=1, sticky="nsew")
bg1 = tk.Frame(app, bg="#F5EAC6")
bg1.grid(row=1, column=2, sticky="nsew")

bg0 = tk.Frame(app, bg="#FAF2D7")
bg0.grid(row=2, column=0, sticky="nsew")
bg0 = tk.Frame(app, bg="#FAF2D7")
bg0.grid(row=2, column=1, sticky="nsew")
bg1 = tk.Frame(app, bg="#F5EAC6")
bg1.grid(row=2, column=2, sticky="nsew")

bg0 = tk.Frame(app, bg="#FAF2D7")
bg0.grid(row=3, column=0, sticky="nsew")
bg0 = tk.Frame(app, bg="#FAF2D7")
bg0.grid(row=3, column=1, sticky="nsew")
bg1 = tk.Frame(app, bg="#F5EAC6")
bg1.grid(row=3, column=2, sticky="nsew")

felt_label = tk.Label(app, text="Feltöltött kép", bg="#FFE178", font=("Arial", 16), width=20, height=2)
felt_label.grid(row=0, column=0, padx=5, pady=5)

szerk_label = tk.Label(app, text="Szerkesztett kép", bg="#FFE178", font=("Arial", 16), width=20, height=2)
szerk_label.grid(row=0, column=1, padx=5, pady=5)

funk_label = tk.Label(app, text="Funkciók", bg="#E8CD6D", font=("Arial", 16), width=20, height=2)
funk_label.grid(row=0, column=2, padx=5, pady=5)

felt_canvas = tk.Canvas(app, bg="#FFFFFF", width=400, height=300)
felt_canvas.grid(row=1, column=0, padx=10, pady=10)

szerk_canvas = tk.Canvas(app, bg="#FFFFFF", width=400, height=300)
szerk_canvas.grid(row=1, column=1, padx=10, pady=10)

felt_button = tk.Button(app, text="Kép feltöltése", bg="#FFE178", font=("Arial", 14), width=15, height=2)
felt_button.grid(row=2, column=0, padx=10, pady=10)

szerk_button = tk.Button(app, text="Kép szerkesztése", bg="#FFE178", font=("Arial", 14), width=15, height=2)
szerk_button.grid(row=2, column=1, padx=10, pady=10)



























app.mainloop()