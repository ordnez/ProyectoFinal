from tkinter import *
from tkinter import messagebox
import pandas as pd

# Función para guardar los datos del usuario en un archivo CSV
def save_data(name, email, cedula):
    data = {'NOMBRE': [name], 'CORREO': [email], 'CEDULA': [cedula]}
    df = pd.DataFrame(data)
    df.to_csv('user_data.csv', mode='a', header=False, index=False)
    messagebox.showinfo("Datos Enviados", "¡Registro guardado exitosamente!")
    show_fuel_price_calculator()

# Función para manejar el evento de envío del formulario
def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    cedula = cedula_entry.get()
    
    # Validación simple: asegúrate de que todos los campos no estén vacíos
    if name.strip() == '' or email.strip() == '' or cedula.strip() == '':
        messagebox.showerror("Error", "Por favor rellene todos los campos.")
    else:
        save_data(name, email, cedula)
        # Limpia los campos después de guardar los datos
        name_entry.delete(0, END)
        email_entry.delete(0, END)
        cedula_entry.delete(0, END)

# Función para mostrar la calculadora de precios de combustible
def show_fuel_price_calculator():
    # Crear una nueva ventana para la calculadora de combustible
    fuel_window = Toplevel(root)
    fuel_window.title("Calculadora de Gasolina")
    fuel_window.geometry("500x350")

    # Función para calcular el precio total según el tipo de gasolina seleccionada
    def calcular_precio():
        # Obtener el tipo de gasolina seleccionada
        gasolina_seleccionada = var.get()
        
        # Definir los precios por galón
        precios = {
            "corriente": 14500,
            "extra": 17500,
            "Diésel": 9000
        }
        
        # Calcular el precio total
        if gasolina_seleccionada in precios:
            precio_por_galon = precios[gasolina_seleccionada]
            galones = int(galones_entry.get())
            total = precio_por_galon * galones
            messagebox.showinfo("Precio Total", f"El precio total es: ${total:.2f}")
        else:
            messagebox.showerror("Error", "Selecciona un tipo de gasolina válido.")

    # Etiqueta y campo de entrada para los galones
    Label(fuel_window, text="Galones de gasolina:").pack(pady=10)
    galones_entry = Entry(fuel_window)
    galones_entry.pack(pady=5)

    # Radio buttons para elegir el tipo de gasolina
    Label(fuel_window, text="Tipo de Gasolina:").pack(pady=10)
    var = StringVar()
    var.set("corriente")

    for gasolina in ["corriente", "extra", "Diésel"]:
        Radiobutton(fuel_window, text=gasolina, variable=var, value=gasolina).pack()

    # Botón para calcular el precio
    Button(fuel_window, text="Calcular Precio", command=calcular_precio).pack(pady=20)

    # Botón para salir del programa
    Button(fuel_window, text="Salir del Programa", command=root.quit).pack(pady=10)


# Configuración de la ventana principal
root = Tk()
root.title("Registro de Usuario y Combustibles Móvil")
root.geometry("500x350")

# Etiqueta y campo de entrada para el nombre
Label(root, text="NOMBRE:").pack(pady=10)
name_entry = Entry(root)
name_entry.pack(pady=5)

# Etiqueta y campo de entrada para el email
Label(root, text="CORREO:").pack(pady=10)
email_entry = Entry(root)
email_entry.pack(pady=5)

# Etiqueta y campo de entrada para la cédula
Label(root, text="CEDULA:").pack(pady=10)
cedula_entry = Entry(root)
cedula_entry.pack(pady=5)

# Botón para enviar el formulario
Button(root, text="Enviar", command=submit_form).pack(pady=20)

# Botón para salir del programa
Button(root, text="Salir del Programa", command=root.quit).pack(pady=10)


# Iniciar el bucle principal de la ventana
root.mainloop()

