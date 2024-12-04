# menu.py
import tkinter as tk
from tkinter import Label, Button, Toplevel
from PIL import Image, ImageTk
import subprocess

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulador del Efecto Doppler")
ancho_ventana = 1000
alto_ventana = 600
root.geometry(f"{ancho_ventana}x{alto_ventana}")
root.resizable(False, False)

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

# Funciones para ejecutar los programas correspondientes
def abrir_frecuencia_obser():
    subprocess.run(['python', 'frecuencia_obser.py'], check=True)

def abrir_velocidad_fuente():
    subprocess.run(['python', 'velocidad_fuente.py'], check=True)

def abrir_velocidad_observador():
    subprocess.run(['python', 'velocidad_observador.py'], check=True)

# Crear botones para las calculadoras y centrarlos
ruta_frecuencia_observada = "imagenes/frecuencia_observada.jpg"
imagen_frecuencia_observada = Image.open(ruta_frecuencia_observada).resize((220, 80), Image.LANCZOS)
imagen_frecuencia_observada_tk = ImageTk.PhotoImage(imagen_frecuencia_observada)

ruta_vel_fuente = "imagenes/vel_fuente.jpg"
imagen_vel_fuente = Image.open(ruta_vel_fuente).resize((220, 80), Image.LANCZOS)
imagen_vel_fuente_tk = ImageTk.PhotoImage(imagen_vel_fuente)

ruta_vel_observador = "imagenes/vel_observ.jpg"
imagen_vel_observador = Image.open(ruta_vel_observador).resize((220, 80), Image.LANCZOS)
imagen_vel_observador_tk = ImageTk.PhotoImage(imagen_vel_observador)

# Botones existentes en el menú
ruta_que_es_btn = "imagenes/que_es_btn.jpg"
imagen_que_es_btn = Image.open(ruta_que_es_btn).resize((300, 80), Image.LANCZOS)
imagen_que_es_btn_tk = ImageTk.PhotoImage(imagen_que_es_btn)

ruta_simulador_btn = "imagenes/simulador_btn.jpg"
imagen_simulador_btn = Image.open(ruta_simulador_btn).resize((300, 80), Image.LANCZOS)
imagen_simulador_btn_tk = ImageTk.PhotoImage(imagen_simulador_btn)

def mostrar_info_doppler():
    ventana_info = Toplevel(root)
    ventana_info.title("¿Qué es el Efecto Doppler?")
    ventana_info.geometry(f"{ancho_ventana}x{alto_ventana}")
    ventana_info.resizable(False, False)

    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2)
    ventana_info.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")

    ruta_definicion = "imagenes/definicion.png"
    imagen_definicion = Image.open(ruta_definicion).resize((ancho_ventana, alto_ventana), Image.LANCZOS)
    imagen_definicion_tk = ImageTk.PhotoImage(imagen_definicion)
    label_definicion = Label(ventana_info, image=imagen_definicion_tk)
    label_definicion.image = imagen_definicion_tk
    label_definicion.pack()

# Crear los botones
boton_frecuencia = Button(root, image=imagen_frecuencia_observada_tk, command=abrir_frecuencia_obser, borderwidth=0)
boton_frecuencia.place(x=620, y=320)

boton_vel_fuente = Button(root, image=imagen_vel_fuente_tk, command=abrir_velocidad_fuente, borderwidth=0)
boton_vel_fuente.place(x=510, y=220)

boton_vel_observador = Button(root, image=imagen_vel_observador_tk, command=abrir_velocidad_observador, borderwidth=0)
boton_vel_observador.place(x=750, y=220)

boton_que_es = Button(root, image=imagen_que_es_btn_tk, command=mostrar_info_doppler, borderwidth=0)
boton_que_es.place(x=580, y=80)

boton_simulador = Button(root, image=imagen_simulador_btn_tk, command=lambda: subprocess.run(['python', 'calculadora.py'], check=True), borderwidth=0)
boton_simulador.place(x=560, y=460)

# Ejecutar el bucle principal
root.mainloop()
