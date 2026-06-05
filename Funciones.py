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

def ordenar_listas(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado):
    """Recibe por parametros las listas del programa, las ordena por insercion usando los dos criterios propios
    -Santiago Perozzi"""
    # Determinar la cantidad total de elementos usando cualquiera de las listas paralelas
    n = len(cod_deuda)
    
    # Recorrer desde el segundo elemento hasta el final de la lista
    for i in range(1, n):
        
        # Guardamos en variables auxiliares los 7 datos del movimiento actual 
        aux_cod     = cod_deuda[i]
        aux_det     = det_deuda[i]
        aux_cat     = categoria[i]
        aux_monto_t = monto_total[i]
        aux_monto_p = monton_pendiente[i]
        aux_venc    = vencimiento[i]
        aux_est     = estado[i]
        
        j = i
        
        # Evaluacion de la insercion y las criterios propios:
        # - Criterio principal: El monto pendiente de la izquierda es menor al actual
        # - Criterio secundario: El detalle de la izquierda es mayor alfabéticamente 
        while j > 0 and (monton_pendiente[j - 1] < aux_monto_p or (monton_pendiente[j - 1] == aux_monto_p and det_deuda[j - 1] > aux_det)):
            
            # Desplazar los datos a la derecha, donde van respecto al dato actual
            cod_deuda[j]        = cod_deuda[j - 1]
            det_deuda[j]        = det_deuda[j - 1]
            categoria[j]        = categoria[j - 1]
            monto_total[j]      = monto_total[j - 1]
            monton_pendiente[j] = monton_pendiente[j - 1]
            vencimiento[j]      = vencimiento[j - 1]
            estado[j]           = estado[j - 1]
            
            # Retroceder un lugar a la izquierda para comparar con el siguiente
            j = j - 1
            
        # Insertar los datos guardados en la posicion correspondiente final
        cod_deuda[j]        = aux_cod
        det_deuda[j]        = aux_det
        categoria[j]        = aux_cat
        monto_total[j]      = aux_monto_t
        monton_pendiente[j] = aux_monto_p
        vencimiento[j]      = aux_venc
        estado[j]           = aux_est

