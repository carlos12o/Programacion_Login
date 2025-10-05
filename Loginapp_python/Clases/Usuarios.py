class Usuario:
    def __init__(self, nombre, apellido, email, username, clave, rol):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.username = username
        self.clave = clave
        self.rol = rol

from Clases.Conector import Conector

class Usuarios:

    def __init__(self):
        self.db = Conector()
    
    def validar_usuarios(self, username, clave):
        sql = "SELECT * from usuarios where username = %s AND clave = %s"
        values = (username, clave)
        return self.db.select(sql, values)
    
    def validarUsuario(self, username, clave):
        return self.validar_usuarios(username, clave)
    
    def registrarUsuarios(self, nombre, apellido, email, username, clave, rol):
        sql = "INSERT INTO usuarios (nombre, apellido, email, username, clave, rol) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (nombre, apellido, email, username, clave, rol)
        return self.db.execute_query(sql, values)