from Equipo import Equipo
from Operaciones import Operaciones


class OperacionesEquipo(Operaciones):

    def __init__(self):
        super().__init__("Equipo")

    def crear(self):
        print("Registrar " + self._entidad)
        marca = input("\tMarca: ")
        modelo = input("\tModelo: ")
        descripcion = input("\tDescripción: ")
        observaciones = input("\tObservaciones: ")
        return Equipo(marca, modelo, descripcion, observaciones)

    def editar(self):
        print("Editar " + self._entidad)
        id_equipo = input("\tIntroduzca ID del equipo: ")
        equipo_obtenido = self._lista.obtener(id_equipo)
        if equipo_obtenido:
            print("Datos del equipo")
            print(equipo_obtenido)
            atributo = int(input("¿Qué atributo modificar?: "))
            if atributo == 1:
                marca = input("\tMarca: ")
                equipo_obtenido.set_marca(marca)
            elif atributo == 2:
                modelo = input("\tModelo: ")
                equipo_obtenido.set_modelo(modelo)
            elif atributo == 3:
                descripcion = input("\tDescripción: ")
                equipo_obtenido.set_descripcion(descripcion)
            elif atributo == 4:
                observaciones = input("\tObservaciones: ")
                equipo_obtenido.set_observaciones(observaciones)
            else:
                print("Atributo no válido")
        else:
            print("Equipo no encontrado")

    def principal(self):
        while True:
            self.sub_menu()
            sub_opcion = int(input("Elija una operación: "))
            if sub_opcion == 1:
                equipo = self.crear()
                self._lista.append(equipo)
            elif sub_opcion == 2:
                print("Lista de " + self._entidad + "s")
                self._lista.show()
            elif sub_opcion == 3:
                self.editar()
            elif sub_opcion == 4:
                print("Eliminar " + self._entidad)
                id_equipo = input("Introduzca ID del equipo: ")
                self._lista.remove(id_equipo)
            elif sub_opcion == 5:
                print("Volviendo al menú")
                break
            else:
                print("Operación incorrecta")
