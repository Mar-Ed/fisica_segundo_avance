import tkinter as tk
from tkinter import messagebox

def calcular_vo():
    try:
        c = float(entry_velocidad_medio.get())  # Velocidad de las ondas en el medio
        vf = float(entry_velocidad_fuente.get())  # Velocidad de la fuente
        fe = float(entry_frecuencia_emitida.get())  # Frecuencia emitida por la fuente
        fo = float(entry_frecuencia_observada.get())  # Frecuencia observada

        if abs(vf) >= c:
            messagebox.showerror("Error", "La fuente no puede moverse más rápido que el medio.")
            return

        # Fórmula para calcular vo
        vo = ((fo / fe) * (c + vf)) - c

        entry_velocidad_observador.delete(0, tk.END)
        entry_velocidad_observador.insert(0, f"{vo:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# Interfaz gráfica
root = tk.Tk()
root.title("Calculadora de Velocidad del Observador")
root.geometry("400x300")

# Títulos y entradas de datos
tk.Label(root, text="Velocidad de las ondas en el medio (c):", anchor="w").grid(row=0, column=0, sticky="w", padx=10, pady=5)
entry_velocidad_medio = tk.Entry(root)
entry_velocidad_medio.insert(0, "343.2")  # Valor por defecto
entry_velocidad_medio.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Velocidad de la fuente (vf):", anchor="w").grid(row=1, column=0, sticky="w", padx=10, pady=5)
entry_velocidad_fuente = tk.Entry(root)
entry_velocidad_fuente.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Frecuencia emitida (fe):", anchor="w").grid(row=2, column=0, sticky="w", padx=10, pady=5)
entry_frecuencia_emitida = tk.Entry(root)
entry_frecuencia_emitida.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Frecuencia observada (fo):", anchor="w").grid(row=3, column=0, sticky="w", padx=10, pady=5)
entry_frecuencia_observada = tk.Entry(root)
entry_frecuencia_observada.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Velocidad del observador (vo):", anchor="w").grid(row=4, column=0, sticky="w", padx=10, pady=5)
entry_velocidad_observador = tk.Entry(root, state="normal")
entry_velocidad_observador.grid(row=4, column=1, padx=10, pady=5)

# Botón para calcular
btn_calcular = tk.Button(root, text="Calcular", command=calcular_vo)
btn_calcular.grid(row=5, columnspan=2, pady=20)

root.mainloop()
