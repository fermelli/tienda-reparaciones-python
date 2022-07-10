from Lista import Lista
from funciones import generarId


class Equipo:

    def __init__(self, marca, modelo, descripcion, observaciones=""):
        self.__id = generarId()
        self.__marca = marca
        self.__modelo = modelo
        self.__descripcion = descripcion
        self.__observaciones = observaciones
        self.__lista_detalle = Lista()

    def __str__(self):
        return "\n\tid: " + self.__id + "\n\t[1] marca: " + self.__marca + "\n\t[2] modelo: " + self.__modelo + "\n\t[3] descripción: " + self.__descripcion + "\n\t[4] observaciones: " + self.__observaciones + "\n"

    def set_marca(self, marca):
        self.__marca = marca

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_observaciones(self, observaciones):
        self.__observaciones = observaciones

    def get_id(self):
        return self.__id

    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_descripcion(self):
        return self.__descripcion

    def get_observaciones(self):
        return self.__observaciones

    def add_detalle(self, detalle):
        self.__lista_detalle.append(detalle)

    def delete_detalle(self, id_detalle):
        self.__lista_detalle.remove(id_detalle)
