from Funciones import *

cod_deuda = []
det_deuda = []
categoria = []
monto_total = []
monton_pendiente = []
vencimiento = []
estado = []

while True:    
    opciones_menu()
    opcion = ingresar_opcionMenu(1,5)
    #analizamos opcion de menu
    if opcion == 5:
        print("Saliendo del sistema.")
        break

    if opcion ==1:
        print ("="*50)
        print("Registrar movimiento: ")

        cod = validar_codigo_deuda()
        
        while buscar_por_codigo(cod_deuda, cod) != -1:
            print("Ese código ya existe. Debe ingresar un código único.")
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

    elif opcion==2:
        print ("="*50)
        print("Eliminar movimiento: ")

        if len(cod_deuda) == 0:
            print("No hay movimientos registrados para eliminar.")
        else:
            cod_buscar = input("Ingrese el código del movimiento que desea eliminar: ").strip()
            
            # 1. Buscar la posición (índice) del código usando la nueva función
            pos = buscar_por_codigo(cod_deuda, cod_buscar)
            
            if pos == -1:
                print("El código ingresado no existe en el sistema.")
            else:
                # 2. Si existe, pasamos el índice a la función de eliminación para verificar estado y borrar
                eliminar_registro(pos, cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)


    elif opcion ==3:
        print ("="*50)
        print("Modificar movimiento: ")

        if len(cod_deuda) == 0:
            print("No hay movimientos registrados para modificar.")
        else:
            cod_buscar = input("Ingrese el código del movimiento que desea modificar: ").strip()

            # Busca la posición con la función del grupo
            pos = buscar_por_codigo(cod_deuda, cod_buscar)

            if pos == -1:
                print("El código ingresado no existe en el sistema.")
            else:
                # Llama a tu función interactiva de modificación
                modificar_registro(pos, cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)


    elif opcion == 4:
        ordenar_listas(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)
        print ("="*50)
        print("Informe: ")
        
        for i in range (len(cod_deuda)):
            print(f"Código: {cod_deuda[i]} | Detalle: {det_deuda[i]} | Categoria: {categoria[i]} | Monto Pendiente: ${monton_pendiente[i]} | Vencimiento: {vencimiento[i]} | Estado: {estado[i]}")

