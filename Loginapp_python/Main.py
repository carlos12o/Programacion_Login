import tkinter as tk
from Formularios.FrmLogin import FrmLogin
from Formularios.FrmRegistro import FrmRegistro

def abrir_login():
    ventana.destroy()
    FrmLogin()

def abrir_registro():
    ventana.destroy()
    FrmRegistro()

ventana = tk.Tk()
ventana.title("Bienvenido")
ventana.geometry("300x200")
ventana.configure(bg="#f3f3f3")

tk.Label(ventana, text="Seleccione una opción", font=("Arial", 14), bg="#f3f3f3").pack(pady=20)
tk.Button(ventana, text="Iniciar Sesión", width=20, command=abrir_login).pack(pady=10)
tk.Button(ventana, text="Registrar Usuario", width=20, command=abrir_registro).pack(pady=10)

ventana.mainloop()