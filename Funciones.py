import time

def opciones_menu():
    """Muestra el menú principal 
    -Gael Conde"""
    print("=" * 50)
    print("\033[32mSISTEMA DE GESTIÓN: SMARTBUDGET CONTROL\033[0m")
    print("=" * 50)
    print("1: Registrar movimiento")
    print("2: Eliminar movimiento")
    print("3: Modificar movimiento")
    print("4: Informe General")
    print("5: Gestionar Categorías (ABM)")
    print("6: Registrar Pago")
    print("7: Listar Pagos Pendientes")
    print("8: Salir")
    print("=" * 50)

def ingresar_opcionMenu(desde, hasta):
    '''Válida ingresar un valor en el rango desde-hasta usando métodos de string
    -Gael Conde'''
    op_str = input("Seleccione una opción: ").strip()
    while not op_str.isdigit() or int(op_str) < desde or int(op_str) > hasta:
        print("\033[31mError: La opción seleccionada no es válida o no es un número.\033[0m")
        op_str = input("Seleccione una opción: ").strip()
    return int(op_str)

def validar_fecha():
    """Pide la fecha de vencimiento y valida que cumpla el formato dd/mm/aaaa.
    -Franco Estevez"""
    while True:
        fecha_str = input("Ingrese la fecha de vencimiento (dd/mm/aaaa): ").strip()
        if len(fecha_str) == 10 and fecha_str[2] == '/' and fecha_str[5] == '/':
            partes = fecha_str.split('/')
            if partes[0].isdigit() and partes[1].isdigit() and partes[2].isdigit():
                dia, mes, anio = int(partes[0]), int(partes[1]), int(partes[2])
                if 1 <= mes <= 12 and 1 <= dia <= 31 and anio >= 2026:
                    try:
                        time.strptime(fecha_str, "%d/%m/%Y")
                        return fecha_str
                    except ValueError:
                        print("\033[31mError: La fecha ingresada no existe en el calendario.\033[0m")
                        continue
        print("\033[31mError: Formato inválido o datos incorrectos. Use dd/mm/aaaa (ej: 18/06/2026).\033[0m")

def validar_estado():
    """Pide el ingreso del estado y valida que sea correcto mediante ciclos.
    -Santiago Perozzi"""
    estados_validos = ["Pendiente", "Pagado Total", "Pagado Parcial", "Vencido"]
    estado_valido = False
    estado_final = ""
   
    while not estado_valido:
        estado_ingresado = input("Ingrese el estado del movimiento (Pendiente, Pagado Total, Pagado Parcial, Vencido): ").strip()
       
        # Compara sin importar mayúsculas/minúsculas
        for estado in estados_validos:
            if estado_ingresado.lower() == estado.lower():
                estado_valido = True
                estado_final = estado  # Guarda el formato exacto de la lista
               
        if not estado_valido:
            print("\033[31mError: Estado ingresado inválido.\033[0m")
           
    return estado_final

def ordenar_listas(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado):
    """Ordena las listas por inserción usando monto pendiente (desc) y detalle (asc).
    -Santiago Perozzi"""
    n = len(cod_deuda)
    for i in range(1, n):
        aux_cod = cod_deuda[i]
        aux_det = det_deuda[i]
        aux_cat = categoria[i]
        aux_monto_t = monto_total[i]
        aux_monto_p = monton_pendiente[i]
        aux_venc = vencimiento[i]
        aux_est = estado[i]
        j = i
        while j > 0 and (monton_pendiente[j - 1] < aux_monto_p or (monton_pendiente[j - 1] == aux_monto_p and det_deuda[j - 1] > aux_det)):
            cod_deuda[j] = cod_deuda[j - 1]
            det_deuda[j] = det_deuda[j - 1]
            categoria[j] = categoria[j - 1]
            monto_total[j] = monto_total[j - 1]
            monton_pendiente[j] = monton_pendiente[j - 1]
            vencimiento[j] = vencimiento[j - 1]
            estado[j] = estado[j - 1]
            j = j - 1
        cod_deuda[j] = aux_cod
        det_deuda[j] = aux_det
        categoria[j] = aux_cat
        monto_total[j] = aux_monto_t
        monton_pendiente[j] = aux_monto_p
        vencimiento[j] = aux_venc
        estado[j] = aux_est

def validar_categoria(categorias_permitidas):
    """Compara el ingreso con una lista de categorías permitidas.
    -Gael Conde"""
    print(f"Categorías válidas: {categorias_permitidas}")
    cat = input("Ingrese la categoría: ").strip().capitalize()
    while cat not in categorias_permitidas:
        print("\033[31mError: Categoría inválida. Seleccione una de la lista.\033[0m")
        cat = input("Ingrese la categoría: ").strip().capitalize()
    return cat

def validar_monto(mensaje):
    """Verifica valores numéricos válidos mayores o iguales a cero.
    -Gael Conde"""
    while True:
        monto_str = input(mensaje).strip()  
        if monto_str.replace('.', '', 1).isdigit():
            monto = float(monto_str)
            if monto >= 0:
                return monto
            else:
                print("\033[31mError: El monto no puede ser negativo.\033[0m")
        else:
            print("\033[31mError: El monto debe ser un valor numérico válido.\033[0m")

def buscar_por_codigo(cod_deuda, codigo_buscado):
    """
    Búsqueda secuencial por código. Recibe la lista de códigos y el código buscado.
    Retorna el índice (posición) donde se encuentra, o -1 si no existe.
    -Franco Estevez, Santiago Perozzi
    """
    posicion = -1
    encontrado = False
    i = 0
    n = len(cod_deuda)
   
    while i < n and not encontrado:
        if cod_deuda[i] == codigo_buscado:
            posicion = i
            encontrado = True 
        i += 1 
       
    return posicion

def validar_codigo_deuda():
    """Ingresa el codigo del movimiento y valida el largo minimo y la repeticion de codigos unificando el formato
    -Santiago Perozzi"""
    codigo = input("Ingrese el código de la deuda (mínimo 4 caracteres): ").strip().upper()
    while len(codigo) < 4:
        print("\033[31mError: El código debe contener al menos 4 caracteres.\033[0m")
        codigo = input("Ingrese el código de la deuda (mínimo 4 caracteres): ").strip().upper()
    return codigo

def validar_detalle():
    """Ingresa el detalle del movimiento y valida que no sea nulo
    -Franco Estevez"""
    detalle = input("Ingrese el detalle del movimiento: ").strip()
    while len(detalle) == 0:
        print("\033[31mError: El detalle no puede quedar vacío.\033[0m")
        detalle = input("Ingrese el detalle del movimiento: ").strip()
    return detalle

def calcular_dias_restantes(fecha_venc_str):
    """Calcula con la libreria time los dias pendientes para la deuda, recibiendo por parametro la fecha de vencimiento
    -Franco Estevez"""
    segundos_actual = time.time()
    fecha_struct = time.strptime(fecha_venc_str, "%d/%m/%Y")
    segundos_venc = time.mktime(fecha_struct)
    diferencia_segundos = segundos_venc - segundos_actual
    dias_restantes = int(diferencia_segundos // 86400)
    if diferencia_segundos < 0 and dias_restantes == 0:
        return -1
    return dias_restantes