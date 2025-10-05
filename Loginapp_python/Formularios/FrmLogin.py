import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Necesitas instalar pillow: pip install pillow
from Clases.Usuarios import Usuarios
import os

class FrmLogin:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("INGRESO AL SISTEMA")
        self.root.geometry("800x500")
        self.root.configure(bg="#f3f3f3")

        # Título
        tk.Label(self.root, text="INGRESO AL SISTEMA", font=("Times New Roman", 22), bg="#f3f3f3").place(x=480, y=40)

        # Imagen logo
        logo_path = os.path.join(os.path.dirname(__file__), "logo_unitecnar.png")
        try:
            logo = Image.open(logo_path)  # Ruta dinámica
            logo = logo.resize((180, 120))
            self.logo_img = ImageTk.PhotoImage(logo)
            tk.Label(self.root, image=self.logo_img, bg="#f3f3f3").place(x=60, y=120)
        except FileNotFoundError:
            print(f"Archivo no encontrado: {logo_path}")

        # Imagen usuario
        user_img_path = os.path.join(os.path.dirname(__file__), "Usuario.png")
        try:
            user_img = Image.open(user_img_path)  # Ruta dinámica
            user_img = user_img.resize((60, 60))
            self.user_photo = ImageTk.PhotoImage(user_img)
            tk.Label(self.root, image=self.user_photo, bg="#f3f3f3").place(x=600, y=90)
        except FileNotFoundError:
            print(f"Archivo no encontrado: {user_img_path}")

        # Etiquetas y campos
        tk.Label(self.root, text="Usuario:", font=("Arial", 14), bg="#f3f3f3").place(x=480, y=170)
        self.username = tk.Entry(self.root, font=("Arial", 14))
        self.username.place(x=580, y=170, width=200)

        tk.Label(self.root, text="Clave:", font=("Arial", 14), bg="#f3f3f3").place(x=480, y=210)
        self.clave = tk.Entry(self.root, show="*", font=("Arial", 14))
        self.clave.place(x=580, y=210, width=200)

        # Botón Iniciar sesión
        self.chk_var = tk.IntVar()
        tk.Checkbutton(self.root, text="Iniciar sesion", variable=self.chk_var, font=("Arial", 12), bg="#f3f3f3").place(x=580, y=250)
        tk.Button(self.root, text="Ingresar", font=("Arial", 12), command=self.ingresar).place(x=680, y=290, width=100)

        self.root.mainloop()

    def ingresar(self):
        user = self.username.get()
        pwd = self.clave.get()
        print(f"Intentando validar usuario: {user}, clave: {pwd}")  # Depuración
        usuarios = Usuarios()
        try:
            resultado = usuarios.validarUsuario(user, pwd)
            print(f"Resultado de la validación: {resultado}")  # Depuración
            if resultado:
                self.root.destroy()
                from Formularios.FrmDashboard import FrmDashboard
                FrmDashboard(resultado[0])
            else:
                messagebox.showerror("Error", "Usuario o clave incorrectos")
        except Exception as e:
            print(f"Error durante la validación: {e}")  # Depuración
            messagebox.showerror("Error", f"Ocurrió un error: {e}")