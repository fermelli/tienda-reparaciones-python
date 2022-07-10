from funciones import generarId


class Detalle:

    def __init__(self, orden_trabajo, equipo, diagnostico, descripcion_problema, estado):
        self.__id = generarId()
        self.__orden_trabajo = orden_trabajo
        self.__equipo = equipo
        self.__diagnostico = diagnostico
        self.__descripcion_problema = descripcion_problema
        self.__estado = estado

    def __str__(self):
        return "\n\tID. orden de trabajo: " + self.__orden_trabajo.get_id() + "\n\tID. equipo: " + self.__equipo.get_id() + "\n\t[1] diagnóstico: " + self.__diagnostico + "\n\t[2] descripción del problema: " + self.__descripcion_problema + "\n\t[3] estado: " + self.__estado + "\n"

    def set_orden_trabajo(self, orden_trabajo):
        self.__orden_trabajo = orden_trabajo

    def set_equipo(self, equipo):
        self.__equipo = equipo

    def set_diagnostico(self, diagnostico):
        self.__diagnostico = diagnostico

    def set_descripcion_problema(self, descripcion_problema):
        self.__descripcion_problema = descripcion_problema

    def set_estado(self, estado):
        self.__estado = estado

    def get_orden_trabajo(self):
        return self.__orden_trabajo

    def get_equipo(self):
        return self.__equipo

    def get_diagnostico(self):
        return self.__diagnostico

    def get_descripcion_problema(self):
        return self.__descripcion_problema

    def get_estado(self):
        return self.__estado
