from OperacionesCliente import OperacionesCliente
from OperacionesEquipo import OperacionesEquipo
from OperacionesUsuario import OperacionesUsuario
from OperacionesOrdenesTrabajo import OperacionesOrdenesTrabajo
from OperacionesOrdenEntrega import OperacionesOrdenEntrega

# Variables globales
operaciones_usuario = OperacionesUsuario()
operaciones_cliente = OperacionesCliente()
operaciones_equipo = OperacionesEquipo()
operaciones_orden_trabajo = OperacionesOrdenesTrabajo(
    operaciones_usuario, operaciones_cliente, operaciones_equipo)
operaciones_orden_entrega = OperacionesOrdenEntrega(operaciones_usuario, operaciones_cliente, operaciones_equipo)



def menu():
    print("---Menú---")
    print("1. Usuarios")
    print("2. Clientes")
    print("3. Equipos")
    print("4. Ordenes de Trabajo")
    print("5. Ordenes de Entrega")
    print("6. Logout")
    print("7. Salir")


# Definicion del programa principal
def principal():
    while True:
        if operaciones_usuario.get_lista().count() == 0:
            operaciones_usuario.crear_admin()
        else:
            if operaciones_usuario.get_usuario_logueado():
                menu()
                opcion = int(input("Elija una opción: "))
                if opcion == 1:
                    if operaciones_usuario.get_usuario_logueado().get_rol() == "admin":
                        operaciones_usuario.principal()
                    else:
                        print("No tiene acceso a esta opción")
                elif opcion == 2:
                    operaciones_cliente.principal()
                elif opcion == 3:
                    operaciones_equipo.principal()
                elif opcion == 4:
                    operaciones_orden_trabajo.principal()
                elif opcion == 5:
                    operaciones_orden_entrega.principal()
                elif opcion == 6:
                    operaciones_usuario.logout()
                elif opcion == 7:
                    print("Saliendo del programa...")
                    break
                else:
                    print("Opción incorrecta")
            else:
                operaciones_usuario.login()


# Ejecucion del programa principal
principal()
