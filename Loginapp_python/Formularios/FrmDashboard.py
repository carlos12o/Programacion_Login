import tkinter as tk
from PIL import Image, ImageTk

class FrmDashboard:
    def __init__(self, usuario):
        self.root = tk.Tk()
        self.root.title("Panel Administrativo")
        self.root.geometry("600x400")
        self.root.configure(bg="#f3f3f3")

        self.usuario = usuario

        menubar = tk.Menu(self.root)
        usuarios_menu = tk.Menu(menubar, tearoff=0)
        usuarios_menu.add_command(label="Administración de usuarios", command=self.mostrar_datos_usuario)
        menubar.add_cascade(label="Usuarios", menu=usuarios_menu)
        self.root.config(menu=menubar)

        self.frame_datos = tk.Frame(self.root, bg="#f3f3f3")
        self.frame_datos.pack(pady=40)

        self.lbl_nombre = tk.Label(self.frame_datos, font=("Arial", 14), bg="#f3f3f3")
        self.lbl_nombre.pack(pady=5)
        self.lbl_email = tk.Label(self.frame_datos, font=("Arial", 14), bg="#f3f3f3")
        self.lbl_email.pack(pady=5)
        self.lbl_rol = tk.Label(self.frame_datos, font=("Arial", 14), bg="#f3f3f3")
        self.lbl_rol.pack(pady=5)

        self.root.mainloop()

    def mostrar_datos_usuario(self):
        nombre_completo = f"{self.usuario[1]} {self.usuario[2]}"
        email = self.usuario[3]
        rol = self.usuario[6] 
        self.lbl_nombre.config(text=f"Nombre: {nombre_completo}")
        self.lbl_email.config(text=f"Email: {email}")
        self.lbl_rol.config(text=f"Rol: {rol}")
