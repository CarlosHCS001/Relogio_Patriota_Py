import tkinter as tk
from tkinter import ttk
from datetime import datetime
import pytz
from PIL import Image, ImageTk
import os

# Dicionário com fuso horário e bandeiras
paises = {
    "Brasil": {"timezone": "America/Sao_Paulo", "bandeira": "bandeiras/brasil.png"},
    "Estados Unidos": {"timezone": "America/New_York", "bandeira": "bandeiras/eua.png"},
    "Japão": {"timezone": "Asia/Tokyo", "bandeira": "bandeiras/japao.png"},
    "Alemanha": {"timezone": "Europe/Berlin", "bandeira": "bandeiras/alemanha.png"},
    "França": {"timezone": "Europe/Paris", "bandeira": "bandeiras/franca.png"}
}

# Janela principal
root = tk.Tk()
root.title("Relógio Criativo")
root.geometry("500x350")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=10, pady=10)

tk.Label(frame, text="Escolha o país:", font=("Arial", 12)).pack()
pais_var = tk.StringVar(value="Brasil")
pais_menu = ttk.Combobox(frame, textvariable=pais_var, values=list(paises.keys()))
pais_menu.pack(pady=5)

canvas = tk.Canvas(frame, width=480, height=250)
canvas.pack(pady=10)

lbl = tk.Label(canvas, text="", font=("Arial", 20, "bold"), bg="white")
lbl.place(relx=0.5, rely=0.85, anchor="center")

img_ref = None

def atualizar():
    global img_ref
    pais = pais_var.get()
    timezone = pytz.timezone(paises[pais]["timezone"])
    agora = datetime.now(timezone)

    # Atualiza texto da data e hora
    texto = agora.strftime("%d/%m/%Y  %H:%M:%S")
    lbl.config(text=texto)

    # Caminho relativo da bandeira
    caminho_bandeira = paises[pais]["bandeira"]

    if os.path.exists(caminho_bandeira):
        img = Image.open(caminho_bandeira)
        img = img.resize((480, 250), Image.Resampling.LANCZOS)
        img_ref = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor="nw", image=img_ref)
        lbl.lift()
    else:
        lbl.config(text=f"Imagem não encontrada:\n{caminho_bandeira}", bg="red")

    root.after(1000, atualizar)

atualizar()
root.mainloop()
