class Nodo:

    def __init__(self, datos=None, siguiente=None):
        self.datos = datos
        self.siguiente = siguiente

    def __str__(self):
        return "\n" + self.datos + "->" + self.siguiente
