from Persona import Persona


class Cliente(Persona):

    def __init__(self, ci, nombre, celular, direccion, observaciones=""):
        super().__init__(ci, nombre, celular, direccion)
        self.__observaciones = observaciones

    def __str__(self):
        return super().__str__() + "\t[5] observaciones: " + self.__observaciones + "\n"

    def set_observaciones(self, observaciones):
        self.__observaciones = observaciones

    def get_observaciones(self):
        return self.__observaciones
