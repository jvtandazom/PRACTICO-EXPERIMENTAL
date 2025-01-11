import tkinter as tk
from tkinter import messagebox

# Clase para manejar los turnos
class Turno:
    def __init__(self, nombre, identificacion, fecha, hora):
        self.nombre = nombre
        self.identificacion = identificacion
        self.fecha = fecha
        self.hora = hora

class AgendaTurnos:
    def __init__(self):
        self.turnos = []

    def agregar_turno(self, turno):
        self.turnos.append(turno)

    def buscar_turnos(self, identificacion):
        return [turno for turno in self.turnos if turno.identificacion == identificacion]

# Crear la agenda y agregar algunos turnos
agenda = AgendaTurnos()
agenda.agregar_turno(Turno("JONATHAN TANDAZO MEDINA", "1726175506", "2025-01-25", "10:00"))
agenda.agregar_turno(Turno("Ana López", "1234567890", "2025-01-12", "11:00"))
agenda.agregar_turno(Turno("Luis Gómez", "1234567890", "2025-01-13", "09:30"))

# Función para buscar turnos desde la interfaz
def buscar_turnos():
    identificacion = entrada_id.get()
    if not identificacion:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa un número de cédula.")
        return

    resultados = agenda.buscar_turnos(identificacion)
    if resultados:
        texto_resultados = "\n".join(
            f"Nombre: {turno.nombre}, Fecha: {turno.fecha}, Hora: {turno.hora}" for turno in resultados
        )
        messagebox.showinfo("Turnos Encontrados", texto_resultados)
    else:
        messagebox.showinfo("Sin resultados", "No se encontraron turnos para esta cédula.")

# Crear la interfaz gráfica
ventana = tk.Tk()
ventana.title("Hospital Eugenio Espejo - Agenda de Turnos")
ventana.geometry("400x300")
ventana.resizable(False, False)

# Encabezado
titulo = tk.Label(ventana, text="Bienvenido al Hospital Eugenio Espejo", font=("Helvetica", 16), fg="blue")
titulo.pack(pady=20)

# Etiqueta y entrada para el ID
tk.Label(ventana, text="Por favor, ingrese su número de cédula:", font=("Helvetica", 12)).pack(pady=10)
entrada_id = tk.Entry(ventana, width=30, font=("Helvetica", 12))
entrada_id.pack(pady=5)

# Botón para buscar turnos
boton_buscar = tk.Button(ventana, text="Consultar Turnos", command=buscar_turnos, bg="green", fg="white", font=("Helvetica", 12))
boton_buscar.pack(pady=20)

# Pie de página
pie = tk.Label(ventana, text="Hospital Eugenio Espejo © 2025", font=("Helvetica", 10), fg="gray")
pie.pack(side="bottom", pady=10)

# Iniciar la ventana
ventana.mainloop()
