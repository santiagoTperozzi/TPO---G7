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
        print("Registrar movimiento: ")
    elif opcion==2:
        print("Eliminar movimiento: ")
    elif opcion ==3:
        print("Modificar movimiento: ")
    elif opcion == 4:
        ordenar_listas(cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado)
        print ("="*50)
        print("Informe: ")
        print ("="*50)
        
        for i in range (len(cod_deuda)):
            print(f"Código: {cod_deuda[i]} | Detalle: {det_deuda[i]} | Categoria: {categoria[i]} | Monto Pendiente: ${monton_pendiente[i]} | Vencimiento: {vencimiento[i]} | Estado: {estado[i]}")

