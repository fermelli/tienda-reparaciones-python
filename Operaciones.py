from Lista import Lista


class Operaciones:

    def __init__(self, entidad):
        self._entidad = entidad
        self._lista = Lista()

    def get_lista(self):
        return self._lista

    def sub_menu(self):
        print("---Submenú de " + self._entidad + "---")
        print("1. Registrar " + self._entidad)
        print("2. Listar " + self._entidad)
        print("3. Actualizar " + self._entidad)
        print("4. Eliminar " + self._entidad)
        print("5. Volver al menú")

    def sub_menu_ordenes(self):
        print("---Submenú de " + self._entidad + "---")
        print("1. Registrar " + self._entidad)
        print("2. Listar " + self._entidad)
        print("3. Eliminar " + self._entidad)
        print("4. Volver al menú")
