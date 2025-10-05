import tkinter as tk
from tkinter import messagebox
from Clases.Usuarios import Usuarios

class FrmRegistro:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Registro de Usuario")
        self.root.geometry("400x400")
        self.root.configure(bg="#f3f3f3")

        tk.Label(self.root, text="Nombre:", bg="#f3f3f3").pack(pady=5)
        self.nombre = tk.Entry(self.root)
        self.nombre.pack()

        tk.Label(self.root, text="Apellido:", bg="#f3f3f3").pack(pady=5)
        self.apellido = tk.Entry(self.root)
        self.apellido.pack()

        tk.Label(self.root, text="Email:", bg="#f3f3f3").pack(pady=5)
        self.email = tk.Entry(self.root)
        self.email.pack()

        tk.Label(self.root, text="Username:", bg="#f3f3f3").pack(pady=5)
        self.username = tk.Entry(self.root)
        self.username.pack()

        tk.Label(self.root, text="Clave:", bg="#f3f3f3").pack(pady=5)
        self.clave = tk.Entry(self.root, show="*")
        self.clave.pack()

        tk.Label(self.root, text="Rol:", bg="#f3f3f3").pack(pady=5)
        self.rol = tk.Entry(self.root)
        self.rol.pack()

        tk.Button(self.root, text="Registrar", command=self.registrar_usuario).pack(pady=20)

        self.root.mainloop()

    def registrar_usuario(self):
        nombre = self.nombre.get()
        apellido = self.apellido.get()
        email = self.email.get()
        username = self.username.get()
        clave = self.clave.get()
        rol = self.rol.get()

        if not (nombre and apellido and email and username and clave and rol):
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        usuarios = Usuarios()
        try:
            usuarios.registrarUsuarios(nombre, apellido, email, username, clave, rol)
            messagebox.showinfo("Éxito", "Usuario registrado correctamente")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo registrar el usuario:\n{e}")