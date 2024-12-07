import tkinter as tk
from tkinter import messagebox

def calcular_frecuencia():
    try:
        c = float(entry_velocidad_medio.get())  # Velocidad de las ondas en el medio
        vf = float(entry_velocidad_fuente.get())  # Velocidad de la fuente
        vo = float(entry_velocidad_observador.get())  # Velocidad del observador
        fe = float(entry_frecuencia_emitida.get())  # Frecuencia emitida por la fuente

        if abs(vf) >= c:
            messagebox.showerror("Error", "La fuente no puede moverse más rápido que el medio.")
            return

        # Fórmula del efecto Doppler
        fo = fe * (c + vo) / (c + vf)

        entry_frecuencia_observada.delete(0, tk.END)
        entry_frecuencia_observada.insert(0, f"{fo:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Interfaz gráfica
root = tk.Tk()

# Cargar la imagen de fondo
bg_fondo = tk.PhotoImage(file='./imagenes/fondo_frecuenc_observ.png')

# Ajustar el tamaño de la ventana al tamaño de la imagen
bg_width = bg_fondo.width()
bg_height = bg_fondo.height()
root.geometry(f"{bg_width}x{bg_height}")

# Centrar la ventana en la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_centrado = (screen_width // 2) - (bg_width // 2)
y_centrado = (screen_height // 2) - (bg_height // 2)
root.geometry(f"{bg_width}x{bg_height}+{x_centrado}+{y_centrado}")

# Deshabilitar la modificación del tamaño de la ventana
root.resizable(False, False)

# Crear un Label para el fondo
label_fondo = tk.Label(root, image=bg_fondo)
label_fondo.place(relwidth=1, relheight=1)

# Cargar y redimensionar las imágenes específicas para cada label
bg_velocidad_medio = tk.PhotoImage(file='./imagenes/label_vel_sonido.png').subsample(4, 4)
bg_velocidad_fuente = tk.PhotoImage(file='./imagenes/label_vel_fuente.png').subsample(4, 4)
bg_velocidad_observador = tk.PhotoImage(file='./imagenes/label_vel_observ.png').subsample(5, 5)
bg_frecuencia_emitida = tk.PhotoImage(file='./imagenes/label_frec_emitida.png').subsample(4, 4)
bg_frecuencia_observada = tk.PhotoImage(file='./imagenes/label_frec_observ.png').subsample(4, 4)

# Etiquetas con imágenes
label_velocidad_medio = tk.Label(root, image=bg_velocidad_medio, compound="left")
label_velocidad_medio.place(x=10, y=220)

label_velocidad_fuente = tk.Label(root, image=bg_velocidad_fuente, compound="left")
label_velocidad_fuente.place(x=10, y=290)

label_velocidad_observador = tk.Label(root, image=bg_velocidad_observador, compound="left")
label_velocidad_observador.place(x=10, y=360)

label_frecuencia_emitida = tk.Label(root, image=bg_frecuencia_emitida, compound="left")
label_frecuencia_emitida.place(x=10, y=430)

label_frecuencia_observada = tk.Label(root, image=bg_frecuencia_observada, compound="left")
label_frecuencia_observada.place(x=520, y=420)

# Entradas de texto
entry_velocidad_medio = tk.Entry(root)
entry_velocidad_medio.insert(0, "343.2")  # Valor por defecto
entry_velocidad_medio.place(x=250, y=240)

entry_velocidad_fuente = tk.Entry(root)
entry_velocidad_fuente.place(x=250, y=310)

entry_velocidad_observador = tk.Entry(root)
entry_velocidad_observador.place(x=250, y=380)

entry_frecuencia_emitida = tk.Entry(root)
entry_frecuencia_emitida.place(x=250, y=450)

entry_frecuencia_observada = tk.Entry(root, state="normal")
entry_frecuencia_observada.place(x=720, y=435)

# Botón para calcular
btn_calcular = tk.Button(root, text="Calcular", command=calcular_frecuencia,
                         bg="#d12e2e", fg="white", font=("Arial", 12, "bold"),
                         relief="flat", borderwidth=2, padx=10, pady=0,
                         highlightthickness=0, bd=0, 
                         activebackground="#006f8e", activeforeground="white")
btn_calcular.config(highlightthickness=1, bd=1)
btn_calcular.place(x=400, y=420)

root.mainloop()
