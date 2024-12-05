import tkinter as tk
from tkinter import messagebox

def calcular_vf():
    try:
        c = float(entry_velocidad_medio.get())  # Velocidad de las ondas en el medio
        vo = float(entry_velocidad_observador.get())  # Velocidad del observador
        fe = float(entry_frecuencia_emitida.get())  # Frecuencia emitida por la fuente
        fo = float(entry_frecuencia_observada.get())  # Frecuencia observada

        if fo < fe and vo == 0:
            messagebox.showerror("Error", "El observador o la fuente deben estar en movimiento.")
            return

        # Fórmula para calcular vf
        vf = (fo / fe * (c + vo)) - c

        entry_velocidad_fuente.delete(0, tk.END)
        entry_velocidad_fuente.insert(0, f"{vf:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Interfaz gráfica
root = tk.Tk()

# Cargar la imagen de fondo
bg_fondo = tk.PhotoImage(file='./imagenes/fondo_veloc_fuente.png')

# Obtener las dimensiones de la imagen de fondo
bg_width = bg_fondo.width()
bg_height = bg_fondo.height()

# Ajustar el tamaño de la ventana al tamaño de la imagen
root.geometry(f"{bg_width}x{bg_height}")

# Crear un Label que ocupe toda la ventana como fondo
label_fondo = tk.Label(root, image=bg_fondo)
label_fondo.place(relwidth=1, relheight=1)  # Esto hace que el fondo ocupe toda la ventana

# Cargar y redimensionar las imágenes específicas para cada label
bg_velocidad_medio = tk.PhotoImage(file='./imagenes/label_vel_sonido.png').subsample(4, 4)
bg_velocidad_observador = tk.PhotoImage(file='./imagenes/label_vel_observ.png').subsample(5, 5)
bg_frecuencia_emitida = tk.PhotoImage(file='./imagenes/label_frec_emitida.png').subsample(4,4)
bg_frecuencia_observada = tk.PhotoImage(file='./imagenes/label_frec_observ.png').subsample(4, 4)
bg_velocidad_fuente = tk.PhotoImage(file='./imagenes/label_vel_fuente.png').subsample(4, 4)

# Etiquetas con imágenes (labels)
label_velocidad_medio = tk.Label(root, image=bg_velocidad_medio, compound="left")
label_velocidad_medio.grid(row=0, column=0, sticky="w", padx=10, pady=5)
label_velocidad_medio.place(x=50, y=220)

label_velocidad_observador = tk.Label(root, image=bg_velocidad_observador, compound="left")
label_velocidad_observador.grid(row=1, column=0, sticky="w", padx=10, pady=5)
label_velocidad_observador.place(x=50, y=290)

label_frecuencia_emitida = tk.Label(root, image=bg_frecuencia_emitida, compound="left")
label_frecuencia_emitida.grid(row=2, column=0, sticky="w", padx=10, pady=5)
label_frecuencia_emitida.place(x=50, y=360)

label_frecuencia_observada = tk.Label(root, image=bg_frecuencia_observada, compound="left")
label_frecuencia_observada.grid(row=3, column=0, sticky="w", padx=10, pady=5)
label_frecuencia_observada.place(x=50, y=430)

label_velocidad_fuente = tk.Label(root, image=bg_velocidad_fuente, compound="left")
label_velocidad_fuente.grid(row=4, column=0, sticky="w", padx=10, pady=5)
label_velocidad_fuente.place(x=520, y=420)

# Entradas de texto (txt_ entradas) con place para posicionarlas al costado de las etiquetas
entry_velocidad_medio = tk.Entry(root)
entry_velocidad_medio.insert(0, "343.2")  # Valor por defecto
entry_velocidad_medio.place(x=300, y=240)  # Posición al costado de la etiqueta

entry_velocidad_observador = tk.Entry(root)
entry_velocidad_observador.place(x=300, y=310)  # Posición al costado de la etiqueta

entry_frecuencia_emitida = tk.Entry(root)
entry_frecuencia_emitida.place(x=300, y=380)  # Posición al costado de la etiqueta

entry_frecuencia_observada = tk.Entry(root)
entry_frecuencia_observada.place(x=300, y=450)  # Posición al costado de la etiqueta

entry_velocidad_fuente = tk.Entry(root, state="normal")
entry_velocidad_fuente.place(x=300, y=500)  # Posición al costado de la etiqueta

# Botón para calcular
btn_calcular = tk.Button(root, text="Calcular", command=calcular_vf)
btn_calcular.grid(row=5, columnspan=2, pady=20)
btn_calcular.place(x=440, y=550)

root.mainloop()
