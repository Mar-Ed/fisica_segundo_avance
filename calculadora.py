import tkinter as tk
from tkinter import messagebox
from main import iniciar_simulacion

def calcular_frecuencia():
    try:
        vf = float(entry_velocidad_fuente.get())  # Velocidad de la fuente
        vo = float(entry_velocidad_observador.get())  # Velocidad del observador
        fe = float(entry_frecuencia_emitida.get())  # Frecuencia emitida por la fuente
        d = float(entry_distancia.get())  # Distancia entre el observador y la fuente

        # Llamada a la simulación, pasando los valores obtenidos
        iniciar_simulacion(vf, vo, fe, d)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Interfaz gráfica
root = tk.Tk()
root.title("Datos de ingreso Efecto Doppler")
root.geometry("400x300")

# Títulos y entradas de datos

tk.Label(root, text="Velocidad de la fuente (vf):", anchor="w").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_velocidad_fuente = tk.Entry(root)
entry_velocidad_fuente.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Velocidad del observador (vo):", anchor="w").grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_velocidad_observador = tk.Entry(root)
entry_velocidad_observador.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Frecuencia de la onda (fe):", anchor="w").grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_frecuencia_emitida = tk.Entry(root)
entry_frecuencia_emitida.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Distancia entre el observador y la fuente (d):", anchor="w").grid(row=4, column=0, sticky="w", padx=10, pady=5)
entry_distancia = tk.Entry(root)
entry_distancia.grid(row=4, column=1, padx=10, pady=5)

# Botón para calcular
btn_calcular = tk.Button(root, text="Calcular", command=calcular_frecuencia)
btn_calcular.grid(row=5, columnspan=2, pady=20)

root.mainloop()
