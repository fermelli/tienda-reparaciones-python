from funciones import generarId
from Lista import Lista


class OrdenTrabajo:

    def __init__(self, usuario, cliente, fecha_hora):
        self.__id = generarId()
        self.__usuario = usuario
        self.__cliente = cliente
        self.__fecha_hora = fecha_hora
        self.__lista_detalle = Lista()

    def __str__(self):
        return "\n\tid: " + self.__id + "\n\tusuario: " + self.__usuario.__str__() + "\n\tcliente: " + \
            self.__cliente.__str__() + "\n\tfecha y hora: " + \
            str(self.__fecha_hora) + "\n\tdetalle: " + \
            self.__lista_detalle.__str__() + "\n----------\n"

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def set_cliente(self, cliente):
        self.__cliente = cliente

    def set_fecha(self, fecha):
        self.__fecha_hora = fecha

    def get_id(self):
        return self.__id

    def get_usuario(self):
        return self.__usuario

    def get_cliente(self):
        return self.__cliente

    def get_fecha(self):
        return self.__fecha_hora

    def add_detalle(self, detalle):
        self.__lista_detalle.append(detalle)

    def delete_detalle(self, id_detalle):
        self.__lista_detalle.remove(id_detalle)
