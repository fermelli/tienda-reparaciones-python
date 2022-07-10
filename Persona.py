from funciones import generarId


class Persona:

    def __init__(self, ci, nombre, celular, direccion):
        self.__id = generarId()
        self.__ci = ci
        self.__nombre = nombre
        self.__celular = celular
        self.__direccion = direccion

    def __str__(self):
        return "\n\tid: " + self.__id + "\n\t[1] ci: " + self.__ci + "\n\t[2] nombre: " + self.__nombre + "\n\t[3] celular: " + self.__celular + "\n\t[4] dirección: " + self.__direccion + "\n"

    def set_ci(self, ci):
        self.__ci = ci

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_celular(self, celular):
        self.__celular = celular

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def get_id(self):
        return self.__id

    def get_ci(self):
        return self.__ci

    def get_nombre(self):
        return self.__nombre

    def get_celular(self):
        return self.__celular

    def get_direccion(self):
        return self.__direccion
