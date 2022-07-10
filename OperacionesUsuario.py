from Operaciones import Operaciones
from Usuario import Usuario
from funciones import encriptar


class OperacionesUsuario(Operaciones):

    def __init__(self):
        super().__init__("Usuario")
        self._usuario_logueado = None

    def get_usuario_logueado(self):
        return self._usuario_logueado

    def crear(self):
        print("Registrar " + self._entidad)
        ci = input("\tCarnet de identidad: ")
        nombre = input("\tNombre: ")
        celular = input("\tCelular: ")
        direccion = input("\tDirección: ")
        usuario = input("\tUsuario: ")
        password = input("\tContraseña: ")
        rol = input("\tRol: ")
        return Usuario(ci, nombre, celular, direccion, usuario, password, rol)

    def crear_admin(self):
        print("Registrar " + self._entidad + " Administrador")
        ci = input("\tCarnet de identidad: ")
        nombre = input("\tNombre: ")
        celular = input("\tCelular: ")
        direccion = input("\tDirección: ")
        usuario = input("\tUsuario: ")
        password = input("\tContraseña: ")
        rol = "admin"
        admin = Usuario(ci, nombre, celular, direccion, usuario, password, rol)
        self._lista.append(admin)
        self._usuario_logueado = admin

    def editar(self):
        print("Editar " + self._entidad)
        id_usuario = input("\tIntroduzca ID del usuario: ")
        usuario_obtenido = self._lista.obtener(id_usuario)
        if usuario_obtenido:
            print("Datos del usuario")
            print(usuario_obtenido)
            atributo = int(input("¿Qué atributo modificar?: "))
            if atributo == 1:
                ci = input("\tCarnet de identidad: ")
                usuario_obtenido.set_ci(ci)
            elif atributo == 2:
                nombre = input("\tNombre: ")
                usuario_obtenido.set_nombre(nombre)
            elif atributo == 3:
                celular = input("\tCelular: ")
                usuario_obtenido.set_celular(celular)
            elif atributo == 4:
                direccion = input("\tDirección: ")
                usuario_obtenido.set_direccion(direccion)
            elif atributo == 5:
                rol = input("\tRol: ")
                usuario_obtenido.set_rol(rol)
            elif atributo == 6:
                usuario = input("\tUsuario: ")
                usuario_obtenido.set_usuario(usuario)
            elif atributo == 7:
                password = input("\tContraseña: ")
                usuario_obtenido.set_password(password)
            else:
                print("Atributo no válido")
        else:
            print("Usuario no encontrado")

    def login(self):
        print("Login")
        usuario = input("\tUsuario: ")
        password = input("\tContraseña: ")
        nodo_usuario_actual = self._lista.head
        usuario_encontrado = None
        while nodo_usuario_actual:
            if nodo_usuario_actual.datos.get_usuario() == usuario and nodo_usuario_actual.datos.get_password() == encriptar(password):
                usuario_encontrado = nodo_usuario_actual.datos
            nodo_usuario_actual = nodo_usuario_actual.siguiente
        if usuario_encontrado:
            print("Acceso concedido")
        else:
            print("Usuario o Contraseña no válidos")
        self._usuario_logueado = usuario_encontrado

    def logout(self):
        print("Logout")
        self._usuario_logueado = None

    def principal(self):
        while True:
            self.sub_menu()
            sub_opcion = int(input("Elija una operación: "))
            if sub_opcion == 1:
                usuario = self.crear()
                self._lista.append(usuario)
            elif sub_opcion == 2:
                print("Lista de " + self._entidad + "s")
                self._lista.show()
            elif sub_opcion == 3:
                self.editar()
            elif sub_opcion == 4:
                print("Eliminar " + self._entidad)
                id_usuario = input("\tIntroduzca ID del usuario: ")
                self._lista.remove(id_usuario)
            elif sub_opcion == 5:
                print("Volviendo al menú")
                break
            else:
                print("Operación incorrecta")
