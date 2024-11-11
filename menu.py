""" import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk  # Necesario instalar Pillow para manejar imágenes

# Crear la ventana principal
root = tk.Tk()
root.title("Simulador del Efecto Doppler")
root.geometry("900x500")  # Ajustar el tamaño de la ventana según sea necesario

# Cargar la imagen de fondo
ruta_imagen = "imagenes/fondo.png"
imagen_fondo = Image.open(ruta_imagen)
imagen_fondo = imagen_fondo.resize((900, 500), Image.ANTIALIAS)  # Redimensionar imagen si es necesario
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

# Crear un label para mostrar la imagen de fondo
label_fondo = Label(root, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)  # Ocupa toda la ventana

# Correr el loop principal de la ventana
root.mainloop()
 """
""" 
import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk  # Necesario para manejar imágenes

# Crear la ventana principal
root = tk.Tk()
root.title("Simulador del Efecto Doppler")
root.geometry("900x500")  # Ajustar el tamaño de la ventana según sea necesario

# Cargar la imagen de fondo
ruta_fondo = "imagenes/fondo.png"
imagen_fondo = Image.open(ruta_fondo)
imagen_fondo = imagen_fondo.resize((900, 500), Image.ANTIALIAS)  # Redimensionar imagen si es necesario
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

# Crear un label para mostrar la imagen de fondo
label_fondo = Label(root, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)  # Ocupa toda la ventana

# Cargar las imágenes para los botones
ruta_que_es_btn = "imagenes/que_es_btn.jpg"
imagen_que_es_btn = Image.open(ruta_que_es_btn)
imagen_que_es_btn = imagen_que_es_btn.resize((200, 50), Image.ANTIALIAS)  # Ajusta el tamaño si es necesario
imagen_que_es_btn_tk = ImageTk.PhotoImage(imagen_que_es_btn)

ruta_simulador_btn = "imagenes/simulador_btn.jpg"
imagen_simulador_btn = Image.open(ruta_simulador_btn)
imagen_simulador_btn = imagen_simulador_btn.resize((200, 50), Image.ANTIALIAS)  # Ajusta el tamaño si es necesario
imagen_simulador_btn_tk = ImageTk.PhotoImage(imagen_simulador_btn)

# Funciones para los botones (puedes personalizarlas)
def mostrar_info_doppler():
    print("Mostrar información sobre el Efecto Doppler")

def iniciar_simulador():
    print("Iniciar simulador del Efecto Doppler")

# Crear botones con las imágenes
boton_que_es = Button(root, image=imagen_que_es_btn_tk, command=mostrar_info_doppler, borderwidth=0)
boton_que_es.place(x=600, y=150)  # Posición del botón ¿Qué es efecto Doppler?

boton_simulador = Button(root, image=imagen_simulador_btn_tk, command=iniciar_simulador, borderwidth=0)
boton_simulador.place(x=600, y=250)  # Posición del botón Simulador del Efecto Doppler

# Correr el loop principal de la ventana
root.mainloop()
 """
""" import tkinter as tk
from tkinter import Label, Button
from PIL import Image, ImageTk  # Necesario para manejar imágenes

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulador del Efecto Doppler")
ancho_ventana = 1000
alto_ventana = 600
root.geometry(f"{ancho_ventana}x{alto_ventana}")  # Ajustar el tamaño de la ventana

# Hacer que la ventana no sea redimensionable
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
imagen_fondo = imagen_fondo.resize((ancho_ventana, alto_ventana), Image.ANTIALIAS)  # Ajustar fondo al nuevo tamaño
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

# Crear un label para mostrar la imagen de fondo
label_fondo = Label(root, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)  # Ocupa toda la ventana

# Cargar las imágenes para los botones y ajustarlas a un tamaño mayor
ruta_que_es_btn = "imagenes/que_es_btn.jpg"
imagen_que_es_btn = Image.open(ruta_que_es_btn)
imagen_que_es_btn = imagen_que_es_btn.resize((300, 80), Image.ANTIALIAS)  # Tamaño más grande para el botón
imagen_que_es_btn_tk = ImageTk.PhotoImage(imagen_que_es_btn)

ruta_simulador_btn = "imagenes/simulador_btn.jpg"
imagen_simulador_btn = Image.open(ruta_simulador_btn)
imagen_simulador_btn = imagen_simulador_btn.resize((300, 80), Image.ANTIALIAS)  # Tamaño más grande para el botón
imagen_simulador_btn_tk = ImageTk.PhotoImage(imagen_simulador_btn)

# Funciones para los botones (puedes personalizarlas)
def mostrar_info_doppler():
    print("Mostrar información sobre el Efecto Doppler")

def iniciar_simulador():
    print("Iniciar simulador del Efecto Doppler")

# Crear botones con las imágenes y centrarlos en la parte derecha de la ventana
boton_que_es = Button(root, image=imagen_que_es_btn_tk, command=mostrar_info_doppler, borderwidth=0)
boton_que_es.place(x=600, y=200)  # Posición ajustada para el botón ¿Qué es efecto Doppler?

boton_simulador = Button(root, image=imagen_simulador_btn_tk, command=iniciar_simulador, borderwidth=0)
boton_simulador.place(x=600, y=320)  # Posición ajustada para el botón Simulador del Efecto Doppler

# Correr el loop principal de la ventana
root.mainloop()
 """
import tkinter as tk
from tkinter import Label, Button, Toplevel
from PIL import Image, ImageTk  # Necesario para manejar imágenes

# Configuración de la ventana principal
root = tk.Tk()
root.title("Simulador del Efecto Doppler")
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
imagen_fondo = imagen_fondo.resize((ancho_ventana, alto_ventana), Image.ANTIALIAS)
imagen_fondo_tk = ImageTk.PhotoImage(imagen_fondo)

# Crear un label para mostrar la imagen de fondo
label_fondo = Label(root, image=imagen_fondo_tk)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Cargar las imágenes para los botones y ajustarlas a un tamaño mayor
ruta_que_es_btn = "imagenes/que_es_btn.jpg"
imagen_que_es_btn = Image.open(ruta_que_es_btn)
imagen_que_es_btn = imagen_que_es_btn.resize((300, 80), Image.ANTIALIAS)
imagen_que_es_btn_tk = ImageTk.PhotoImage(imagen_que_es_btn)

ruta_simulador_btn = "imagenes/simulador_btn.jpg"
imagen_simulador_btn = Image.open(ruta_simulador_btn)
imagen_simulador_btn = imagen_simulador_btn.resize((300, 80), Image.ANTIALIAS)
imagen_simulador_btn_tk = ImageTk.PhotoImage(imagen_simulador_btn)

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
    imagen_definicion = imagen_definicion.resize((ancho_ventana, alto_ventana), Image.ANTIALIAS)
    imagen_definicion_tk = ImageTk.PhotoImage(imagen_definicion)

    # Mostrar la imagen en la nueva ventana
    label_definicion = Label(ventana_info, image=imagen_definicion_tk)
    label_definicion.image = imagen_definicion_tk  # Necesario para evitar que la imagen se elimine
    label_definicion.pack()

# Función para el simulador (placeholder)
def iniciar_simulador():
    print("Iniciar simulador del Efecto Doppler")

# Crear botones con las imágenes y centrarlos en la parte derecha de la ventana
boton_que_es = Button(root, image=imagen_que_es_btn_tk, command=mostrar_info_doppler, borderwidth=0)
boton_que_es.place(x=600, y=200)

boton_simulador = Button(root, image=imagen_simulador_btn_tk, command=iniciar_simulador, borderwidth=0)
boton_simulador.place(x=600, y=320)

# Correr el loop principal de la ventana
root.mainloop()
