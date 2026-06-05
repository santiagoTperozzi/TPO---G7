def opciones_menu():
    """funcion menu principal del programa
    -Santiago Perozzi"""
    print("=" * 50)
    print("SISTEMA DE GESTIÓN: SMARTBUDGET CONTROL")
    print("=" * 50)
    print("1: Registrar movimiento")
    print("2: Eliminar movimiento")
    print("3: Modificar movimiento")
    print("4: Informe")
    print("5: Salir")
    print("=" * 50)

def ingresar_opcionMenu(desde, hasta):
    '''válida ingresar un valor en el rango desde-hasta
    retorna el valor ingresado del teclado
    -Santiago Perozzi'''
    op = int(input("Seleccione una opción:"))
    while op<desde or op>hasta:
        print("La opción seleccionada no es válida")
        op = int(input("Seleccione una opción:"))
    return op


def validar_mes():
    """Pide el ingreso del mes y valida que sea correcto
    -Santiago Perozzi"""

    mes = int(input("Ingrese el mes de vencimiento del movimiento (1-12): "))

    while mes <= 0 or mes > 12:
        print ("Mes ingresado invalido")
        mes = int(input("Ingrese el mes de vencimiento del movimiento (1-12): "))
    
    return mes

def validar_estado():
    """pide el ingreso del estado y valida que sea correcto
    -Santiago Perozzi"""

    estado = int(input("Ingrese el estado del movimiento (1_Pendiente, 2_Pagado Total, 3_Pagado Parcial, 4_Vencido): "))

    while estado <= 0 or estado > 4:
        print("Estado ingresado invalido")
        estado = int(input("Ingrese el estado del movimiento (1_Pendiente, 2_Pagado Total, 3_Pagado Parcial, 4_Vencido): "))
    
    if estado == 1:
        estado = "Pendiente"
    elif estado == 2:
        estado = "Pagado Total"
    elif estado == 3:
        estado = "Pagado Parcial"
    else:
        estado = "Vencido"
    
    return estado

