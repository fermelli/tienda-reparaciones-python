from Persona import Persona
from funciones import encriptar


class Usuario(Persona):

    def __init__(self, ci, nombre, celular, direccion, usuario, password, rol):
        super().__init__(ci, nombre, celular, direccion)
        self.__usuario = usuario
        self.__password = encriptar(password)
        self.__rol = rol

    def __str__(self):
        return super().__str__() + "\t[5] rol: " + self.__rol + "\n\t[6] usuario: " + self.__usuario + "\n\t[7] password: " + self.__password + "\n"

    def set_rol(self, rol):
        self.__rol = rol

    def set_usuario(self, usuario):
        self.__usuario = encriptar(usuario)

    def set_password(self, password):
        self.__password = encriptar(password)

    def get_rol(self):
        return self.__rol

    def get_password(self):
        return self.__password

    def get_usuario(self):
        return self.__usuario
