from tkinter import *
from tkinter import messagebox

# Función para calcular el precio total según el tipo de gasolina seleccionada
def calcular_precio():
    # Obtener el tipo de gasolina seleccionada
    gasolina_seleccionada = var.get()
    
    # Definir los precios por galon
    precios = {
        "corriente": 14500,
        "extra": 17500,
        "Diésel": 9000
    }
    
    # Calcular el precio total
    if gasolina_seleccionada in precios:
        precio_por_litro = precios[gasolina_seleccionada]
        litros = int(litros_entry.get())
        total = precio_por_litro * litros
        messagebox.showinfo("Precio Total", f"El precio total es: ${total:.2f}")
    else:
        messagebox.showerror("Error", "Selecciona un tipo de gasolina válido.")

# Función para cerrar la sesión
def cerrar_sesion():
    root.destroy()

# Función para salir completamente del programa
def salir_programa():
    root.quit()
    root.destroy()

# Configuración de la ventana principal
root = Tk()
root.title("Calculadora de Gasolina")
root.geometry("500x300")

# Etiqueta y campo de entrada para los litros
Label(root, text="galones de gasolina:").pack(pady=10)
litros_entry = Entry(root)
litros_entry.pack(pady=5)

# Radio buttons para elegir el tipo de gasolina
Label(root, text="Tipo de Gasolina:").pack(pady=10)
var = StringVar()
var.set("corriente")

for gasolina in ["corriente", "extra", "Diésel"]:
    Radiobutton(root, text=gasolina, variable=var, value=gasolina).pack()

# Botón para calcular el precio
Button(root, text="Calcular Precio", command=calcular_precio).pack(pady=10)

# Botón para salir del programa
Button(root, text="Salir del Programa", command=salir_programa).pack(pady=10)

# Iniciar el bucle principal de la ventana
root.mainloop()
