from multiprocessing.connection import Client
from Operaciones import Operaciones
from Cliente import Cliente


class OperacionesCliente(Operaciones):

    def __init__(self):
        super().__init__("Cliente")

    def crear(self):
        print("Registrar " + self._entidad)
        ci = input("\tCarnet de identidad: ")
        nombre = input("\tNombre: ")
        celular = input("\tCelular: ")
        direccion = input("\tDirección: ")
        observaciones = input("\tObservaciones: ")
        return Cliente(ci, nombre, celular, direccion, observaciones)

    def editar(self):
        print("Editar " + self._entidad)
        id_cliente = input("\tIntroduzca ID del cliente: ")
        cliente_obtenido = self._lista.obtener(id_cliente)
        if cliente_obtenido:
            print("Datos del cliente")
            print(cliente_obtenido)
            atributo = int(input("¿Qué atributo modificar?: "))
            if atributo == 1:
                ci = input("\tCarnet de identidad: ")
                cliente_obtenido.set_ci(ci)
            elif atributo == 2:
                nombre = input("\tNombre: ")
                cliente_obtenido.set_nombre(nombre)
            elif atributo == 3:
                celular = input("\tCelular: ")
                cliente_obtenido.set_celular(celular)
            elif atributo == 4:
                direccion = input("\tDirección: ")
                cliente_obtenido.set_direccion(direccion)
            elif atributo == 5:
                observaciones = input("\tObservaciones: ")
                cliente_obtenido.set_observaciones(observaciones)
            else:
                print("Atributo no válido")
        else:
            print("Cliente no encontrado")

    def principal(self):
        while True:
            self.sub_menu()
            sub_opcion = int(input("Elija una operación: "))
            if sub_opcion == 1:
                cliente = self.crear()
                self._lista.append(cliente)
            elif sub_opcion == 2:
                print("Lista de " + self._entidad + "s")
                self._lista.show()
            elif sub_opcion == 3:
                self.editar()
            elif sub_opcion == 4:
                print("Eliminar " + self._entidad)
                id_cliente = input("Introduzca ID del cliente: ")
                self._lista.remove(id_cliente)
            elif sub_opcion == 5:
                print("Volviendo al menú")
                break
            else:
                print("Operación incorrecta")
