from Lista import Lista
from Operaciones import Operaciones
from OrdenTrabajo import OrdenTrabajo
import datetime
from Detalle import Detalle


class OperacionesOrdenesTrabajo(Operaciones):

    def __init__(self, operaciones_usuario, operaciones_cliente, operaciones_equipo):
        super().__init__("Orden de Trabajo")
        self.__operaciones_usuario = operaciones_usuario
        self.__operaciones_cliente = operaciones_cliente
        self.__operaciones_equipo = operaciones_equipo

    def crear(self):
        print("Registrar " + self._entidad)
        usuario_logueado = self.__operaciones_usuario.get_usuario_logueado()
        print("Registado por: " + usuario_logueado.get_usuario())

        cliente = self.recuperar_o_registrar_cliente()

        fecha_hora = datetime.datetime.now()

        orden_trabajo = self.registrar_orden_trabajo(
            usuario_logueado, cliente, fecha_hora)

        return orden_trabajo

    def recuperar_o_registrar_cliente(self):
        cliente = None
        while not cliente:
            print("Registro de Cliente")
            print("1. Elegir cliente desde la lista")
            print("2. Registrar cliente nuevo")
            alternativa = int(input("\tEscoja una alternativa: "))
            if alternativa == 1:
                if self.__operaciones_cliente.get_lista().count() > 0:
                    self.__operaciones_cliente.get_lista().show()
                    id_cliente = input("\tIntroduzca ID del cliente: ")
                    cliente = self.__operaciones_cliente.get_lista().obtener(id_cliente)
                else:
                    print("La lista de clientes no tiene registros")
            elif alternativa == 2:
                cliente = self.__operaciones_cliente.crear()
                self.__operaciones_cliente.get_lista().append(cliente)
            else:
                print("Intente otra vez")

            if cliente:
                print("Finalizó registro de cliente")
        return cliente

    def registrar_orden_trabajo(self, usuario_logueado, cliente, fecha_hora):
        orden_trabajo = OrdenTrabajo(usuario_logueado, cliente, fecha_hora)

        lista_equipos_registrados = Lista()
        while True:
            equipo = None
            print("Registro de Equipos")
            print("1. Elegir equipo desde la lista")
            print("2. Registrar equipo nuevo")
            print("3. Finalizar")
            alternativa = int(input("\tEscoja una alternativa: "))
            if alternativa == 1:
                if self.__operaciones_equipo.get_lista().count() > 0:
                    self.__operaciones_equipo.get_lista().show()
                    id_equipo = input("\tIntroduzca ID del equipo: ")
                    if lista_equipos_registrados.obtener(id_equipo):
                        print("El equipo ya esta registrado")
                    else:
                        equipo = self._lista.obtener(id_equipo)
                else:
                    print("La lista de equipos no tiene registros")
            elif alternativa == 2:
                equipo = self.__operaciones_equipo.crear()
                self.__operaciones_equipo.get_lista().append(equipo)
            elif alternativa == 3:
                if lista_equipos_registrados.count() > 0:
                    print("Finalizó registro de equipos y detalles")
                    break
                else:
                    print("Debe registrar por lo menos un equipo")
            else:
                print("Alternativa no válida")

            if (alternativa == 1 or alternativa == 2) and equipo:
                lista_equipos_registrados.append(equipo)
                print("Registro del Detalle")
                diagnostico = input("\tDiagnóstico: ")
                descripcion_problema = input("\tDescripción del problema: ")
                estado = input("\tEstado: ")
                detalle = Detalle(orden_trabajo, equipo,
                                  diagnostico, descripcion_problema, estado)
                orden_trabajo.add_detalle(detalle)
                equipo.add_detalle(detalle)
        return orden_trabajo

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
                print("Eliminar "+self._entidad)
                id_ordenTrabajo = input("Introduzca ID de la "+self._entidad+": ")
                self._lista.remove(id_ordenTrabajo)
            elif sub_opcion == 4:
                print("Volviendo al menú")
                break
            else:
                print("Operación incorrecta")
