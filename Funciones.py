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

def validar_categoria():
    """
    Compara el ingreso con una lista de categorías permitidas 
    usando operadores de pertenencia.
    - Franco Estevez
    """
    categorias_permitidas = ["Tarjeta", "Préstamo", "Educación", "Vivienda", "Servicios", "Salud", "Entretenimiento", "Otro"]
    
    print("\nCategorías válidas: Tarjeta, Préstamo, Educación, Vivienda, Servicios, Salud, Entretenimiento, Otro")
    cat = input("Ingrese la categoría: ").strip().capitalize()
    
    # Uso de operador de pertenencia 'not in' para validar
    while cat not in categorias_permitidas:
        print("Categoría inválida. Intente nuevamente.")
        cat = input("Ingrese la categoría: ").strip().capitalize()
        
    return cat

def validar_monto(mensaje):
    """
    Verifica que los valores numéricos (con decimales) sean mayores o iguales a cero.
    - Franco Estevezi
    """
    monto = float(input(mensaje))
    
    # Uso de operador de comparación para asegurar valores >= 0
    while monto < 0:
        print("Error: El monto no puede ser negativo.")
        monto = float(input(mensaje))
        
    return monto

def buscar_por_codigo(cod_deuda, codigo_buscado):
    """
    Búsqueda secuencial por código. Recibe la lista de códigos y el código buscado.
    Retorna el índice (posición) donde se encuentra, o -1 si no existe.
    - Franco Estevez
    """
    posicion = -1
    encontrado = False
    i = 0
    n = len(cod_deuda)
    
    # Ciclo combinado con una bandera booleana
    while i < n and not encontrado:
        if cod_deuda[i] == codigo_buscado:
            posicion = i
            encontrado = True  # Corta el ciclo al encontrarlo
        i += 1
        
    return posicion

def eliminar_registro(indice, cod_deuda, det_deuda, categoría, monto_total, monton_pendiente, vencimiento, estado):
    """
    Recibe el índice del elemento. Verifica si el estado es 'Pagada Total'.
    Si es correcto, procede a eliminar el registro de las listas paralas.
    - Franco Estevez    """
    # Verifica si el estado en esa posición es "Pagada Total"
    if estado[indice] == "Pagada Total":
        cod_deuda.pop(indice)
        det_deuda.pop(indice)
        categoría.pop(indice)
        monto_total.pop(indice)
        monton_pendiente.pop(indice)
        vencimiento.pop(indice)
        estado.pop(indice)
        print("¡El movimiento ha sido eliminado de todas las listas con éxito!")
    else:
        print(f"No se puede eliminar: El estado actual es '{estado[indice]}'. Solo se permite eliminar en estado 'Pagada Total'.")

def validar_codigo_deuda():
    """Verifica mediante operadores lógicos y funciones básicas que la cadena ingresada tenga al menos 4 caracteres alfanuméricos.
    - Gael Conde """
    codigo = input("Ingrese el código de la deuda (mínimo 4 caracteres): ").strip()
    while len(codigo) < 4:
        print("Error: El código debe contener al menos 4 caracteres.")
        codigo = input("Ingrese el código de la deuda (mínimo 4 caracteres): ").strip()
    return codigo

def validar_detalle():
    """Asegura que la referencia sobre el motivo del movimiento no se encuentre vacía.
    - Gael Conde """
    detalle = input("Ingrese el detalle del movimiento: ").strip()
    while len(detalle) == 0:
        print("Error: El detalle no puede quedar vacío.")
        detalle = input("Ingrese el detalle del movimiento: ").strip()
    return detalle

def modificar_registro(indice, cod_deuda, det_deuda, categoría, monto_total, monton_pendiente, vencimiento, estado):
    """Recibe el índice del elemento a modificar y permite alterar de forma interactiva y validada los atributos específicos elegidos por el usuario sin alterar el código identificador.
    - Gael Conde """
    print(f"\nModificando el movimiento con código: {cod_deuda[indice]}")
    print("--------------------------------------------------")
    
    # Modificar detalle
    print(f"Detalle actual: {det_deuda[indice]}")
    cambiar_det = input("¿Desea modificar el detalle? (s/n): ").strip().lower()
    if cambiar_det == "s":
        det_deuda[indice] = validar_detalle()
        
    # Modificar categoría
    print(f"Categoría actual: {categoría[indice]}")
    cambiar_cat = input("¿Desea modificar la categoría? (s/n): ").strip().lower()
    if cambiar_cat == "s":
        categoría[indice] = validar_categoria()
        
    # Modificar monto total
    print(f"Monto total actual: ${monto_total[indice]}")
    cambiar_mt = input("¿Desea modificar el monto total? (s/n): ").strip().lower()
    if cambiar_mt == "s":
        monto_total[indice] = validar_monto("Ingrese el nuevo Monto Total: $")
        
    # Modificar monto pendiente
    print(f"Monto pendiente actual: ${monton_pendiente[indice]}")
    cambiar_mp = input("¿Desea modificar el monto pendiente? (s/n): ").strip().lower()
    if cambiar_mp == "s":
        monton_pendiente[indice] = validar_monto("Ingrese el nuevo Monto Pendiente: $")
        
    # Modificar mes de vencimiento
    print(f"Mes de vencimiento actual: {vencimiento[indice]}")
    cambiar_mes = input("¿Desea modificar el mes de vencimiento? (s/n): ").strip().lower()
    if cambiar_mes == "s":
        vencimiento[indice] = validar_mes()
        
    # Modificar estado de pago
    print(f"Estado de pago actual: {estado[indice]}")
    cambiar_est = input("¿Desea modificar el estado de pago? (s/n): ").strip().lower()
    if cambiar_est == "s":
        estado[indice] = validar_estado()
        
    print("\n¡El movimiento ha sido modificado con éxito en todas las listas paralelas")


