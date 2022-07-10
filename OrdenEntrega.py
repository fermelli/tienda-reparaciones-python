from funciones import generarId

class OrdenEntrega:

    def __init__(self, cliente, equipo, fecha_hora, costo):
        self.__id = generarId()
        self.__cliente = cliente
        self.__equipo = equipo
        self.__fecha_hora = fecha_hora
        self.__costo = costo

    def __str__(self):
        return "\n\tid: " + self.__id + "\n\tCliente: " + self.__cliente + "\n\tEquipo: " + \
            self.__equipo + "\n\tCosto Total: " + self.__costo + "\n\tfecha y hora: " + \
            str(self.__fecha_hora) + "\n"

    def get_id(self):
        return self.__id