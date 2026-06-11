from Funciones import *


def registrar_movimiento(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado, categorias_permitidas):
    """Función modularizada para dar de alta un registro (Opción 1)."""
    print("="*50)
    print("Registrar movimiento: ")
     
    cod = validar_codigo_deuda()
    while buscar_por_codigo(cod_deuda, cod) != -1:
        print("\033[31mError: Ese código ya existe. Debe ingresar un código único.\033[0m")
        cod = validar_codigo_deuda()
       
    det = validar_detalle()
    cat = validar_categoria(categorias_permitidas)
    m_total = validar_monto("Ingrese el Monto Total: $")
   
    m_pend = m_total
    est = "Pendiente"
    fecha_venc = validar_fecha()


    cod_deuda.append(cod)
    det_deuda.append(det)
    categoria.append(cat)
    monto_total.append(m_total)
    monton_pendiente.append(m_pend)
    vencimiento.append(fecha_venc)
    estado.append(est)
    print("¡Movimiento registrado con éxito!")


def eliminar_registro(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado):
    """Busca y elimina un registro si su estado es 'Pagada Total' (Opción 2)."""
    print("="*50)
    print("Eliminar movimiento: ")
    if len(cod_deuda) == 0:
        print("No hay movimientos registrados para eliminar.")
        return


    cod_buscar = input("Ingrese el código del movimiento que desea eliminar: ").strip().upper()
    indice = buscar_por_codigo(cod_deuda, cod_buscar)
   
    if indice == -1:
        print("\033[31mEl código ingresado no existe en el sistema.\033[0m")
    elif estado[indice] == "Pagada Total" or estado[indice] == "Pagado Total":
        cod_deuda.pop(indice)
        det_deuda.pop(indice)
        categoria.pop(indice)
        monto_total.pop(indice)
        monton_pendiente.pop(indice)
        vencimiento.pop(indice)
        estado.pop(indice)
        print("¡El movimiento ha sido eliminado de todas las listas con éxito!")
    else:
        print(f"\033[31mNo se puede eliminar: El estado actual es '{estado[indice]}'. Solo se permite eliminar en estado 'Pagada Total'.\033[0m")


def modificar_registro(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado, categorias_permitidas):
    """Busca y permite alterar los atributos específicos elegidos por el usuario (Opción 3)."""
    print("="*50)
    print("Modificar movimiento: ")
    if len(cod_deuda) == 0:
        print("No hay movimientos registrados para modificar.")
        return


    # CORRECCIÓN AQUÍ: Se añadió .upper()
    cod_buscar = input("Ingrese el código del movimiento que desea modificar: ").strip().upper()
    indice = buscar_por_codigo(cod_deuda, cod_buscar)
   
    while indice == -1:
        print("\033[31mEl código ingresado no existe en el sistema.\033[0m")
        # CORRECCIÓN AQUÍ: Se añadió .upper()
        cod_buscar = input("Ingrese el código del movimiento que desea modificar: ").strip().upper()
        indice = buscar_por_codigo(cod_deuda, cod_buscar)
       
    print(f"\nModificando el movimiento con código: {cod_deuda[indice]}")
    print("--------------------------------------------------")
   
    if input("¿Desea modificar el detalle? (s/n): ").strip().lower() == "s":
        det_deuda[indice] = validar_detalle()
    if input("¿Desea modificar la categoría? (s/n): ").strip().lower() == "s":
        categoria[indice] = validar_categoria(categorias_permitidas)
    if input("¿Desea modificar el monto total? (s/n): ").strip().lower() == "s":
        monto_total[indice] = validar_monto("Ingrese el nuevo Monto Total: $")
    if input("¿Desea modificar el monto pendiente? (s/n): ").strip().lower() == "s":
        monton_pendiente[indice] = validar_monto("Ingrese el nuevo Monto Pendiente: $")
    if input("¿Desea modificar la fecha de vencimiento? (s/n): ").strip().lower() == "s":
        vencimiento[indice] = validar_fecha()
    if input("¿Desea modificar el estado de pago? (s/n): ").strip().lower() == "s":
        estado[indice] = validar_estado()
       
    print("\n¡El movimiento ha sido modificado con éxito!")


def informe_general(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado):
    """Genera el Informe General ordenado de movimientos (Opción 4)."""
    print("\033[32m" + "="*50)
    print("INFORME GENERAL DE MOVIMIENTOS")
    print("="*50 + "\033[0m")
   
    if len(cod_deuda) == 0:
        print("No hay movimientos registrados.")
    else:
        ordenar_listas(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)
        print("Movimientos ordenados por Monto Pendiente (Descendente) y Detalle (Ascendente):")
        for i in range(len(cod_deuda)):
            dias = calcular_dias_restantes(vencimiento[i])
            print(f"Código: {cod_deuda[i]} | Detalle: {det_deuda[i]} | Categoria: {categoria[i]} | Total: ${monto_total[i]} | Pendiente: ${monton_pendiente[i]} | Vence: {vencimiento[i]} ({dias} días rest.) | Estado: {estado[i]}")




def abm_categorias(categorias_permitidas, categoria_movimientos):
    """
    Administración de Categorías: Alta, Modificación y Baja.
    Restringe la eliminación si la categoría está en uso.
    - Gael Conde & Santiago Perozzi (Corregido)
    """
    op = ""
    while op != "4":
        print("\n\033[32m" + "="*50)
        print("GESTIÓN DE CATEGORÍAS (ABM)")
        print("="*50 + "\033[0m")
        print("1: Alta de categoría")
        print("2: Modificación de categoría")
        print("3: Baja de categoría")
        print("4: Volver al menú principal")
        print("-" * 50)
       
        op = input("Seleccione una opción de gestión: ").strip()
       
        if op == "1":
            nueva = input("Ingrese el nombre de la nueva categoría: ").strip().capitalize()
            if nueva == "":
                print("\033[31mError: El nombre no puede estar vacío.\033[0m")
            elif nueva in categorias_permitidas:
                print("\033[31mError: La categoría ya existe.\033[0m")
            else:
                categorias_permitidas.append(nueva)
                print(f"\033[32m¡Categoría '{nueva}' dada de Alta con éxito!\033[0m")
               
        elif op == "2":
            print(f"Categorías actuales: {categorias_permitidas}")
            vieja = input("Ingrese la categoría que desea modificar: ").strip().capitalize()
            if vieja in categorias_permitidas:
                nueva = input("Ingrese el nuevo nombre para la categoría: ").strip().capitalize()
                if nueva != "" and nueva not in categorias_permitidas:
                    idx = categorias_permitidas.index(vieja)
                    categorias_permitidas[idx] = nueva
                   
                    # Modificación en cascada en los movimientos actuales
                    for i in range(len(categoria_movimientos)):
                        if categoria_movimientos[i] == vieja:
                            categoria_movimientos[i] = nueva
                    print("\033[32m¡Categoría modificada con éxito en el sistema y en los movimientos!\033[0m")
                else:
                    print("\033[31mError: Nombre inválido o ya existente.\033[0m")
            else:
                print("\033[31mError: La categoría seleccionada no existe.\033[0m")
               
        elif op == "3":
            print(f"Categorías actuales: {categorias_permitidas}")
            target = input("Ingrese la categoría que desea dar de Baja: ").strip().capitalize()
            if target in categorias_permitidas:
                # Restricción de seguridad
                if target in categoria_movimientos:
                    print("\033[31mRestricción de Seguridad: No se puede eliminar. Esta categoría tiene movimientos asociados.\033[0m")
                else:
                    categorias_permitidas.remove(target)
                    print(f"\033[32m¡Categoría '{target}' dada de Baja con éxito!\033[0m")
            else:
                print("\033[31mError: La categoría seleccionada no existe.\033[0m")
               
        elif op == "4":
            print("Volviendo al menú principal...")
        else:
            print("\033[31mError: Opción inválida.\033[0m")


def reporte_pagos_pendientes(cod_deuda, det_deuda, vencimiento, monton_pendiente, estado):
    print("\033[32m" + "="*50)
    print("INFORME DE PAGOS PENDIENTES")
    print("="*50 + "\033[0m")
    hay_pendientes = False
    for i in range(len(cod_deuda)):
        if estado[i] != "Pagada Total" and estado[i] != "Pagado Total":
            hay_pendientes = True
            dias = calcular_dias_restantes(vencimiento[i])
            if dias < 0:
                print(f"\033[31m[VENCIDO] Código: {cod_deuda[i]} | Detalle: {det_deuda[i]} | Vencimiento: {vencimiento[i]} | Días rest.: {dias} | Pendiente: ${monton_pendiente[i]}\033[0m")
            else:
                print(f"Código: {cod_deuda[i]} | Detalle: {det_deuda[i]} | Vencimiento: {vencimiento[i]} | Días rest.: {dias} | Pendiente: ${monton_pendiente[i]}")
    if not hay_pendientes:
        print("Excelente: No se registran pagos pendientes en el sistema.")


def registrar_pago(cod_deuda, monton_pendiente, estado):
    print("\033[32m" + "="*50)
    print("REGISTRO DE PAGOS")
    print("="*50 + "\033[0m")
    # CORRECCIÓN AQUÍ: Se añadió .upper()
    codigo = input("Ingrese el código del movimiento: ").strip().upper()
    pos = buscar_por_codigo(cod_deuda, codigo)
   
    if pos == -1:
        print("\033[31mError: El código de movimiento no existe.\033[0m")
        return
    if estado[pos] == "Pagada Total" or estado[pos] == "Pagado Total":
        print("Este movimiento ya se encuentra cancelado ('Pagada Total').")
        return
       
    print(f"Monto pendiente actual: ${monton_pendiente[pos]}")
    pago = validar_monto("Ingrese el monto a pagar: $")
   
    if pago > monton_pendiente[pos]:
        print("\033[31mError: El pago no puede exceder el monto pendiente actual.\033[0m")
    elif pago == monton_pendiente[pos]:
        monton_pendiente[pos] = 0
        estado[pos] = "Pagada Total"
        print("¡Pago Total registrado! El movimiento ha sido cancelado.")
    else:
        monton_pendiente[pos] = int(monton_pendiente[pos] - pago)
        estado[pos] = "Pagado Parcial"
        print(f"Pago Parcial registrado. Nuevo saldo pendiente: ${monton_pendiente[pos]}")


def main():
    # Estructuras de datos (Listas paralelas)
    cod_deuda = []
    det_deuda = []
    categoria = []
    monto_total = []
    monton_pendiente = []
    vencimiento = []  
    estado = []
   
    # Categorías iniciales
    categorias_permitidas = ["Tarjeta", "Prestamo", "Educacion", "Vivienda", "Servicios", "Salud", "Entretenimiento", "Otro"]
   
    opciones_menu()
    op = ingresar_opcionMenu(1, 8)


    while op != 8:
        if op == 1:
            # Registrar movimiento
            registrar_movimiento(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado, categorias_permitidas)
           
        elif op == 2:
            # Eliminar movimiento (Usa la función modularizada)
            eliminar_registro(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)
           
        elif op == 3:
            # Modificar movimiento (Usa la función modularizada)
            modificar_registro(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado, categorias_permitidas)


        elif op == 4:
            # Informe General de Movimientos
            informe_general(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)
                   
        elif op == 5:
            # Gestión de Categorías (ABM)
            abm_categorias(categorias_permitidas, categoria)
           
        elif op == 6:
            # Registrar Pago
            registrar_pago(cod_deuda, monton_pendiente, estado)
           
        elif op == 7:
            # Listar Pagos Pendientes
            reporte_pagos_pendientes(cod_deuda, det_deuda, vencimiento, monton_pendiente, estado)
           
        # Volver a pedir la opción dentro del ciclo
        opciones_menu()
        op = ingresar_opcionMenu(1, 8)


    print("\n\033[32mGracias por utilizar SMARTBUDGET CONTROL. ¡Hasta luego!\033[0m")


main()
