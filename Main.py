from Funciones import *

def opcion_1 (cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado):
    """Opcion 1 del menu: permite el alta de nuevos movimientos, validando bajo diferentes criterios todos los datos
    -Gael Conde"""
    print ("="*50)
    print("Registrar movimiento: ")

    cod = validar_codigo_deuda()
        
    while buscar_por_codigo(cod_deuda, cod) != -1:
        print("Ese código ya existe. Debe ingresar un código único.")
        cod = validar_codigo_deuda()

    cod = validar_codigo_deuda()

    det = validar_detalle()

    cat = validar_categoria()
    m_total = validar_monto("Ingrese el Monto Total: $")
    m_pend = validar_monto("Ingrese el Monto Pendiente: $")
    mes = validar_mes()
    est = validar_estado()

    cod_deuda.append(cod)
    det_deuda.append(det)
    categoria.append(cat)
    monto_total.append(m_total)
    monton_pendiente.append(m_pend)
    vencimiento.append(mes)
    estado.append(est)
    print("¡Movimiento registrado con éxito!")

def opcion_2 (cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado):
    """Opcion 2 del menu: permite la eliminacion de un movimiento en caso de que ya este pagado
    -..."""
    print ("="*50)
    print("Eliminar movimiento: ")

    if len(cod_deuda) == 0:
        print("No hay movimientos registrados para eliminar.")
    else:
        cod_buscar = input("Ingrese el código del movimiento que desea eliminar: ").strip()
        
        # 1. Buscar la posición (índice) del código usando la nueva función
        pos = buscar_por_codigo(cod_deuda, cod_buscar)
        
        while pos == -1:
            print("El código ingresado no existe en el sistema.")
            cod_buscar = input("Ingrese el código del movimiento que desea eliminar: ").strip()
            pos = buscar_por_codigo(cod_deuda, cod_buscar)
        
        eliminar_registro(pos, cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)

def opcion_3 (cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado):
    """Opcion 3 del menu: busca el codigo de un movimiento en el sistema y permite modificar sus datos
    -..."""
    print ("="*50)
    print("Modificar movimiento: ")

    if len(cod_deuda) == 0:
        print("No hay movimientos registrados para modificar.")
    else:
        cod_buscar = input("Ingrese el código del movimiento que desea modificar: ").strip()
        # Busca la posición con la función del grupo
        pos = buscar_por_codigo(cod_deuda, cod_buscar)

        while pos == -1:
            print("El código ingresado no existe en el sistema.")
            cod_buscar = input("Ingrese el código del movimiento que desea modificar: ").strip()
            pos = buscar_por_codigo(cod_deuda, cod_buscar)
        
        modificar_registro(pos, cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)

def opcion_4 (cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado):
    """Opcion 4 del menu: Ordena las listas por una insercion de dos criterios, luego imprime un informe del estado de todos los movimientos
    -Santiago Perozzi"""
    ordenar_listas(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)
    print ("="*50)
    print("Informe: ")
        
    for i in range (len(cod_deuda)):
        print(f"Código: {cod_deuda[i]} | Detalle: {det_deuda[i]} | Categoria: {categoria[i]} | Monto Pendiente: ${monton_pendiente[i]} | Vencimiento: {vencimiento[i]} | Estado: {estado[i]}")

def opcion_5 ():
    """Opcion 5 del menu: finaliza el programa
    -Santiago Perozzi"""
    print("Saliendo del sistema.")

def main ():
    cod_deuda = []
    det_deuda = []
    categoria = []
    monto_total = []
    monton_pendiente = []
    vencimiento = []
    estado = []

    opciones_menu()
    op = ingresar_opcionMenu(1,5)

    while op != 5:    
        
        #analizamos opcion de menu        
        if op ==1:
            opcion_1(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)
            
        elif op==2:
            opcion_2(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)

        elif op ==3:
            opcion_3(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)

        elif op == 4:
            opcion_4(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)
        
        opciones_menu()
        op = ingresar_opcionMenu(1,5)

        if op == 5:
            opcion_5()

main() 
