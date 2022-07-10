from Nodo import Nodo


class Lista:

    def __init__(self, nodo=None):
        self.head = nodo

    def __str__(self):
        actual = self.head
        strData = ""
        while actual:
            strData = strData + "\t\t" + actual.datos.__str__()
            actual = actual.siguiente
        return strData

    def appendHead(self, datos):
        nuevoNodo = Nodo(datos)
        nuevoNodo.siguiente = self.head
        self.head = nuevoNodo

    def show(self):
        actual = self.head
        print("[ ", end="")
        while actual:
            print(actual.datos, end=" ")
            actual = actual.siguiente
        print("]")

    def append(self, datos):
        nuevoNodo = Nodo(datos)
        if self.head:
            nodoActual = self.head
            while nodoActual:
                if nodoActual.siguiente == None:
                    ultimoNodo = nodoActual
                nodoActual = nodoActual.siguiente
            ultimoNodo.siguiente = nuevoNodo
        else:
            self.head = nuevoNodo

    def clear(self):
        self.head = None

    def count(self):
        contadorNodos = 0
        nodoActual = self.head
        while nodoActual:
            contadorNodos = contadorNodos + 1
            nodoActual = nodoActual.siguiente
        return contadorNodos

    def pop(self):
        nodoActual = self.head
        while nodoActual:
            if nodoActual.siguiente == None:
                nodoUltimo = nodoActual
            else:
                nodoPenultimo = nodoActual
            nodoActual = nodoActual.siguiente
        nodoPenultimo.siguiente = None
        return nodoUltimo

    def remove(self, id):
        nodoActual = self.head
        while nodoActual:
            if nodoActual == self.head and nodoActual.datos.get_id() == id:
                self.head = nodoActual.siguiente
            if nodoActual.siguiente != None and nodoActual.siguiente.datos.get_id() == id:
                nodoAux = nodoActual.siguiente.siguiente
                nodoActual.siguiente = None
                nodoActual.siguiente = nodoAux
            nodoActual = nodoActual.siguiente

    def obtener(self, id):
        nodoActual = self.head
        while nodoActual:
            if nodoActual.datos.get_id() == id:
                return nodoActual.datos
            nodoActual = nodoActual.siguiente
