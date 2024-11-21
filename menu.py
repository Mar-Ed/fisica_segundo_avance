# menu.py
import tkinter as tk
from tkinter import Label, Button, Toplevel
from PIL import Image, ImageTk 
from main import iniciar_simulacion
import threading 
import webbrowser 
# Configuración de la ventana principal
root = tk.Tk()
root.title("Comportamiento del Efecto Doppler")
ancho_ventana = 1000
alto_ventana = 600
root.geometry(f"{ancho_ventana}x{alto_ventana}")  # Ajustar el tamaño de la ventana
root.resizable(False, False)  # Evitar que la ventana sea redimensionable

# Centrando la ventana en la pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
posicion_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
posicion_y = (alto_pantalla // 2) - (alto_ventana // 2)
root.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

# Cargar la imagen de fondo
ruta_fondo = "imagenes/fondo.png"
imagen_fondo = Image.open(ruta_fondo)
imagen_fondo = imagen_fondo.resize((ancho_ventana, alto_ventana), Image.LANCZOS)
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

# Crear un label para mostrar la imagen de fondo
label_fondo = Label(root, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Cargar las imágenes para los botones y ajustarlas a un tamaño mayor
ruta_que_es_btn = "imagenes/que_es_btn.jpg"
imagen_que_es_btn = Image.open(ruta_que_es_btn)
imagen_que_es_btn = imagen_que_es_btn.resize((300, 80), Image.LANCZOS)
imagen_que_es_btn_tk = ImageTk.PhotoImage(imagen_que_es_btn)

ruta_simulador_btn = "imagenes/comportamiento_btn.jpg"
imagen_simulador_btn = Image.open(ruta_simulador_btn)
imagen_simulador_btn = imagen_simulador_btn.resize((300, 80), Image.LANCZOS)
imagen_simulador_btn_tk = ImageTk.PhotoImage(imagen_simulador_btn)

ruta_simulador_web_btn = "imagenes/simulador_btn.jpg"
imagen_simulador_web_btn = Image.open(ruta_simulador_web_btn)
imagen_simulador_web_btn = imagen_simulador_web_btn.resize((300, 80), Image.LANCZOS)
imagen_simulador_web_btn_tk = ImageTk.PhotoImage(imagen_simulador_web_btn)
# Función para mostrar una nueva ventana con la definición del Efecto Doppler
def mostrar_info_doppler():
    # Crear una nueva ventana con el mismo tamaño que la principal
    ventana_info = Toplevel(root)
    ventana_info.title("¿Qué es el Efecto Doppler?")
    ventana_info.geometry(f"{ancho_ventana}x{alto_ventana}")
    ventana_info.resizable(False, False)

    # Centrar la nueva ventana en la pantalla
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)
    ventana_info.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    # Cargar la imagen de definición
    ruta_definicion = "imagenes/definicion.png"
    imagen_definicion = Image.open(ruta_definicion)
    imagen_definicion = imagen_definicion.resize((ancho_ventana, alto_ventana), Image.LANCZOS)
    imagen_definicion_tk = ImageTk.PhotoImage(imagen_definicion)

    # Mostrar la imagen en la nueva ventana
    label_definicion = Label(ventana_info, image=imagen_definicion_tk)
    label_definicion.image = imagen_definicion_tk  # Necesario para evitar que la imagen se elimine
    label_definicion.pack()

# Función para el simulador
def iniciar_simulador():
    iniciar_simulacion()

def abrir_simulacion_web():
    url = "https://www.educaplus.org/game/efecto-doppler"
    webbrowser.open(url)
# Crear botones con las imágenes y centrarlos en la parte derecha de la ventana
boton_que_es = Button(root, image=imagen_que_es_btn_tk, command=mostrar_info_doppler, borderwidth=0)
boton_que_es.place(x=600, y=100)

boton_simulador = Button(root, image=imagen_simulador_btn_tk, command=iniciar_simulador, borderwidth=0)
boton_simulador.place(x=600, y=220)

boton_simulador_doppler = Button(root, image=imagen_simulador_btn_tk, command=abrir_simulacion_web, borderwidth=0)
boton_simulador_doppler.place(x=600, y=340)
# Ejecuta el loop principal de la ventana
root.mainloop()
