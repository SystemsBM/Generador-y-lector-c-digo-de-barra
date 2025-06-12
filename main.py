import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import threading
from pyzbar.pyzbar import decode
import numpy as np
import barcode
from barcode.writer import ImageWriter
import os

# ---------------- GENERADOR ------------------
def generar_codigo_barras():
    texto = entrada_texto.get()
    if not texto.isdigit() or len(texto) not in [12, 13]:
        messagebox.showerror("Error", "Ingrese un número de 12 o 13 dígitos para EAN-13.")
        return
    ean = barcode.get('ean13', texto.zfill(12), writer=ImageWriter())
    nombre_archivo = "codigo_barras"
    ruta = ean.save(nombre_archivo)
    mostrar_imagen(f"{nombre_archivo}.png")

def mostrar_imagen(ruta_img):
    img = Image.open(ruta_img)
    img = img.resize((300, 150))
    img_tk = ImageTk.PhotoImage(img)
    etiqueta_img.config(image=img_tk)
    etiqueta_img.image = img_tk

# ---------------- LECTOR ------------------
def leer_codigo():
    def escanear():
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            for barcode_data in decode(frame):
                datos = barcode_data.data.decode('utf-8')
                puntos = barcode_data.polygon
                cv2.polylines(frame, [np.array([(pt.x, pt.y) for pt in puntos])], True, (0, 255, 0), 2)
                cv2.putText(frame, datos, (puntos[0].x, puntos[0].y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                resultado_var.set(f"Código detectado: {datos}")
            cv2.imshow("Lector de Códigos - ESC para salir", frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC
                break
        cap.release()
        cv2.destroyAllWindows()

    threading.Thread(target=escanear).start()

# ---------------- INTERFAZ ------------------
ventana = tk.Tk()
ventana.title("Código de Barras (Supermercado)")
ventana.geometry("420x500")

frame = ttk.Frame(ventana, padding=20)
frame.pack(fill="both", expand=True)

entrada_texto = ttk.Entry(frame, width=30)
entrada_texto.pack(pady=10)
entrada_texto.insert(0, "123456789012")  # Valor por defecto

btn_generar = ttk.Button(frame, text="Generar Código de Barras (EAN-13)", command=generar_codigo_barras)
btn_generar.pack(pady=5)

etiqueta_img = tk.Label(frame)
etiqueta_img.pack(pady=10)

btn_leer = ttk.Button(frame, text="Leer Código con Cámara", command=leer_codigo)
btn_leer.pack(pady=5)

resultado_var = tk.StringVar()
label_resultado = ttk.Label(frame, textvariable=resultado_var, foreground="green", font=("Arial", 11))
label_resultado.pack(pady=15)

ventana.mainloop()
