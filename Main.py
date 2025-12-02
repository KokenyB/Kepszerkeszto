from PIL import Image
import PIL
import requests
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler
import torch
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

#//-------------------------------------------------------------------------------------------------------------------------
#//definíciók, funkciók:

model_id = "timbrooks/instruct-pix2pix"
pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    safety_checker=None
    low_cpu_mem_usage=True
)
pipe.to("cudo")
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

url = "https://raw.githubusercontent.com/timothybrooks/instruct-pix2pix/main/imgs/example.jpg"


def belep(event):
    if prompt_text.get('1.0', "end-1c") == placeholder:
        prompt_text.delete('1.0', "end-1c")
        prompt_text.config(fg="black")

felt_kep = None
szerk_pil = None
szerk_kep = None
szerk_prompt = ""
imgcount = 0

def kepfeltoltes():
    global felt_kep, felt_pil
    file_utvonala = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )
    if file_utvonala:
        felt_pil = Image.open(file_utvonala).convert("RGB")
        kp = felt_pil.resize((400, 300))

        felt_kep = ImageTk.PhotoImage(kp)
        felt_canvas.create_image(0, 0, anchor="nw", image=felt_kep)

def kepszerkesztes():
    global szerk_kep, szerk_pil, szerk_prompt
    text = prompt_text.get("1.0", "end-1c")
    final_prompt = (szerk_prompt + " " + text).strip()
    if not final_prompt:
        final_prompt = "Make minor edits"
    result = pipe(
        prompt=final_prompt,
        image=felt_pil,
        num_inference_steps=10,  
        image_guidance_scale=1.0
    )
    szerk_pil = result.images[0]
    kp = szerk_pil.resize((400, 300))
    szerk_kep = ImageTk.PhotoImage(kp)
    szerk_canvas.create_image(0, 0, anchor="nw", image=szerk_kep)
    
def kepletoltes(url):
    global imgcount, szerk_pil
    if szerk_pil:
        filename = f"szerkesztett_{imgcount}.png"
        szerk_pil.save(filename)
        imgcount += 1
        print(f"Kép elmentve: {filename}")

def funkciovalasztas(c):
    global szerk_prompt
    if c == 1:
        funk1_canvas.config(bg="#00FF00")
        funk2_canvas.config(bg="#FF0000")
        funk3_canvas.config(bg="#FF0000")
        funk4_canvas.config(bg="#FF0000")
        funk5_canvas.config(bg="#FF0000")
        funk6_canvas.config(bg="#FF0000")
        szerk_prompt = ("Keretezd be a képen található szövegeket!")
    elif c == 2:
        funk2_canvas.config(bg="#00FF00")
        funk1_canvas.config(bg="#FF0000")
        funk3_canvas.config(bg="#FF0000")
        funk4_canvas.config(bg="#FF0000")
        funk5_canvas.config(bg="#FF0000")
        funk6_canvas.config(bg="#FF0000")
        szerk_prompt = ("Vágd körbe a képen található szövegeket!")
    elif c == 3:
        funk3_canvas.config(bg="#00FF00")
        funk1_canvas.config(bg="#FF0000")
        funk2_canvas.config(bg="#FF0000")
        funk4_canvas.config(bg="#FF0000")
        funk5_canvas.config(bg="#FF0000")
        funk6_canvas.config(bg="#FF0000")
        szerk_prompt = ("Illeszd a képre a szöveget: ")
    elif c == 4:
        funk4_canvas.config(bg="#00FF00")
        funk1_canvas.config(bg="#FF0000")
        funk2_canvas.config(bg="#FF0000")
        funk3_canvas.config(bg="#FF0000")
        funk5_canvas.config(bg="#FF0000")
        funk6_canvas.config(bg="#FF0000")
        szerk_prompt = ("Csak a kép hátterét módosítsd! ")
    elif c == 5:
        funk5_canvas.config(bg="#00FF00")
        funk1_canvas.config(bg="#FF0000")
        funk2_canvas.config(bg="#FF0000")
        funk3_canvas.config(bg="#FF0000")
        funk4_canvas.config(bg="#FF0000")
        funk6_canvas.config(bg="#FF0000")
        szerk_prompt = ("Csak a kép fényerősségét módosítsd! ")
    elif c == 6:
        funk6_canvas.config(bg="#00FF00")
        funk1_canvas.config(bg="#FF0000")
        funk2_canvas.config(bg="#FF0000")
        funk3_canvas.config(bg="#FF0000")
        funk4_canvas.config(bg="#FF0000")
        funk5_canvas.config(bg="#FF0000")
        szerk_prompt = ("Vág körbe a képen a kért tárgyakat: ")

#//-------------------------------------------------------------------------------------------------------------------------
#//Kinézet
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

felt_button = tk.Button(app, text="Kép feltöltése", bg="#FFE178", font=("Arial", 14), width=15, height=2, command=kepfeltoltes)
felt_button.grid(row=2, column=0, padx=10, pady=10)

prompt_text = tk.Text(app, bg="#FFFFFF", font=("Arial", 12), width=40, height=10)
prompt_text.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=10, pady=10)
placeholder = "Írd be ide a kívánt változtatásokat..."
prompt_text.insert('1.0', placeholder)
prompt_text.config(fg="gray")
prompt_text.bind("<FocusIn>", belep)

szerk_frame = tk.Frame(app, bg="#FAF2D7")
szerk_frame.grid(row=2, column=1, sticky="nsew")
szerk_frame.columnconfigure(0, weight=1)
szerk_frame.columnconfigure(1, weight=1)
szerk_frame.rowconfigure(0, weight=1)

szerk_button = tk.Button(szerk_frame, text="Kép szerkesztése", bg="#FFE178", font=("Arial", 14), width=15, height=2, command=kepszerkesztes)
szerk_button.grid(row=0, column=0, padx=10, pady=10)

let_button = tk.Button(szerk_frame, text="Kép letöltése", bg="#FFE178", font=("Arial", 14), width=15, height=2, command=kepletoltes)
let_button.grid(row=0, column=1, padx=10, pady=10)


funk_frame = tk.Frame(app, bg="#F5EAC6")
funk_frame.grid(row=1, column=2, rowspan=3, sticky="nsew")
funk_frame.columnconfigure(0, weight=2)
funk_frame.columnconfigure(1, weight=1)
funk_frame.rowconfigure(0, weight=1)
funk_frame.rowconfigure(1, weight=1)
funk_frame.rowconfigure(2, weight=1)
funk_frame.rowconfigure(3, weight=1)
funk_frame.rowconfigure(4, weight=1)
funk_frame.rowconfigure(5, weight=1)

funk1_button = tk.Button(funk_frame, text="Szöveg felismerése", bg="#E0C76A", font=("Arial", 12), command=lambda: funkciovalasztas(1))
funk1_button.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
funk1_canvas = tk.Canvas(funk_frame, bg="#FF0000", width=60, height=60)
funk1_canvas.grid(row=0, column=1)

funk2_button = tk.Button(funk_frame, text="Felismert szöveg körbevágása", bg="#E0C76A", font=("Arial", 12), command=lambda: funkciovalasztas(2))
funk2_button.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
funk2_canvas = tk.Canvas(funk_frame, bg="#FF0000", width=60, height=60)
funk2_canvas.grid(row=1, column=1)

funk3_button = tk.Button(funk_frame, text="Szöveg kére illesztése", bg="#E0C76A", font=("Arial", 12), command=lambda: funkciovalasztas(3))
funk3_button.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)
funk3_canvas = tk.Canvas(funk_frame, bg="#FF0000", width=60, height=60)
funk3_canvas.grid(row=2, column=1)

funk4_button = tk.Button(funk_frame, text="Háttér módosítása", bg="#E0C76A", font=("Arial", 12), command=lambda: funkciovalasztas(4))
funk4_button.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)
funk4_canvas = tk.Canvas(funk_frame, bg="#FF0000", width=60, height=60)
funk4_canvas.grid(row=3, column=1)

funk5_button = tk.Button(funk_frame, text="Fényerő módosítása", bg="#E0C76A", font=("Arial", 12), command=lambda: funkciovalasztas(5))
funk5_button.grid(row=4, column=0, sticky="nsew", padx=5, pady=5)
funk5_canvas = tk.Canvas(funk_frame, bg="#FF0000", width=60, height=60)
funk5_canvas.grid(row=4, column=1)

funk6_button = tk.Button(funk_frame, text="Felismert tárgyak körbevágása", bg="#E0C76A", font=("Arial", 12), command=lambda: funkciovalasztas(6))
funk6_button.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)
funk6_canvas = tk.Canvas(funk_frame, bg="#FF0000", width=60, height=60)
funk6_canvas.grid(row=5, column=1)

app.mainloop()
