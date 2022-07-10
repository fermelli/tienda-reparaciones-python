from Operaciones import Operaciones
from OrdenEntrega import OrdenEntrega
import datetime


class OperacionesOrdenEntrega(Operaciones):

    def __init__(self, operaciones_usuario, operaciones_cliente, operaciones_equipo):
        super().__init__("Orden de Entrega")
        self.__operaciones_usuario = operaciones_usuario
        self.__operaciones_cliente = operaciones_cliente
        self.__operaciones_equipo = operaciones_equipo

    def crear(self):
        print("Registrar " + self._entidad)
        usuario_logueado = self.__operaciones_usuario.get_usuario_logueado()
        print("Registado por: " + usuario_logueado.get_usuario())

        if (self.__operaciones_cliente.get_lista().count()>0):
            self.__operaciones_cliente.get_lista().show()
            id_cliente = input("\tIntroduzca ID del cliente: ")
            cliente = self.__operaciones_cliente.get_lista().obtener(id_cliente)
            nom_cliente = cliente.get_nombre()
            if (self.__operaciones_equipo.get_lista().count() > 0):
                self.__operaciones_equipo.get_lista().show()
                id_equipo = input("\tIntroduzca ID del equipo: ")
                equipo = self.__operaciones_equipo.get_lista().obtener(id_equipo)
                nom_equipo = equipo.get_marca()
                fecha_hora = datetime.datetime.now()
                costo = input('Ingrse el costo total: ')
                return OrdenEntrega(nom_cliente, nom_equipo, fecha_hora, costo)
            else:
                print('No hay equipos')
        else:
            print('No hay clientes')

    def principal(self):
        while True:
            self.sub_menu_ordenes()
            sub_opcion = int(input("Elija una operación: "))
            if sub_opcion == 1:
                orden_trabajo = self.crear()
                self._lista.append(orden_trabajo)
            elif sub_opcion == 2:
                print("Lista de " + self._entidad + "s")
                self._lista.show()
            elif sub_opcion == 3:
                print("Eliminar "+ self._entidad)
                id_ordenEntraga = input("Introduzca ID de la "+self._entidad+": ")
                self._lista.remove(id_ordenEntraga)
            elif sub_opcion == 4:
                print("Volviendo al menú")
                break
            else:
                print("Operación incorrecta")
