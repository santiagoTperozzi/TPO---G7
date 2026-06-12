SmartBudget Control
Sistema de Administración Financiera Personal - Versión Actualizada

Descripción del Proyecto
SmartBudget Control es una aplicación interactiva desarrollada en Python para la interfaz de línea de comandos. Su propósito es centralizar la administración y el análisis de los gastos y compromisos económicos del hogar. El sistema permite organizar formalmente obligaciones financieras tales como tarjetas de crédito, préstamos, servicios y suscripciones, facilitando la planificación económica familiar y previniendo atrasos en los pagos pendientes mediante alertas y cálculos de vencimiento.

Alcance Funcional
El proyecto implementa una solución de gestión en memoria a través de un menú estructurado con las siguientes opciones:

1. Registrar movimiento (Alta)
Permite la incorporación de nuevos compromisos financieros al sistema. Incluye la validación estricta de los datos de entrada: códigos alfanuméricos únicos de un mínimo de 4 caracteres, fechas de vencimiento reales, montos mayores o iguales a cero, y categorías y estados de pago predefinidos. La información se almacena de forma sincronizada.

2. Eliminar movimiento (Baja)
Permite la remoción de un registro mediante la búsqueda de su código de deuda. Como regla de negocio orientada a preservar el historial financiero, la eliminación solo es procedente si el estado de pago del movimiento es estrictamente "Pagada Total" o "Pagado Total".

3. Modificar movimiento (Modificación)
Permite la actualización interactiva de los atributos de un registro existente (detalle, categoría, montos, mes de vencimiento o estado de pago). El usuario puede elegir específicamente qué campo alterar, preservando el código identificador original.

4. Informe General
Presenta un listado ordenado y formateado de todos los movimientos registrados, incluyendo el cálculo en tiempo real de los días restantes para el vencimiento. El ordenamiento de las listas se realiza mediante el método de inserción aplicando un doble criterio:

Criterio Principal: De forma descendente (de mayor a menor) según el monto pendiente de pago.

Criterio Secundario: En caso de igualdad en los montos, se ordena de forma ascendente (alfabéticamente) según el detalle de la deuda.

5. Gestionar Categorías (ABM)
Módulo de administración para las categorías del sistema. Permite:

Alta: Crear nuevas categorías.

Modificación: Cambiar el nombre de una categoría existente (actualizando en cascada todos los movimientos que la utilicen).

Baja: Eliminar categorías, restringido por seguridad si la categoría tiene movimientos financieros asociados.

6. Registrar Pago
Permite ingresar pagos a una deuda específica. El sistema evalúa el monto ingresado, impidiendo que supere la deuda actual. Automáticamente deduce el monto abonado, actualiza el saldo pendiente y ajusta el estado del movimiento a "Pagado Parcial" o "Pagada Total" según corresponda.

7. Listar Pagos Pendientes
Genera un reporte exclusivo de las deudas que aún no han sido canceladas. El sistema calcula los días restantes para el pago y resalta en color rojo aquellas deudas cuyo plazo ya se encuentra [VENCIDO].

Estructura Técnica y Tecnologías
Lenguaje de programación: Python 3.x

Estructuras de datos: Siete listas paralelas para la gestión síncrona de los datos (cod_deuda, det_deuda, categoria, monto_total, monton_pendiente, vencimiento, estado).

Arquitectura de Software: Diseño modular dividido en dos archivos principales:

Funciones.py: Módulo independiente que encapsula la lógica de validación de entradas, menús, algoritmos de búsqueda (secuencial), ordenamiento (inserción) y cálculos de tiempo.

Main.py: Archivo principal que orquesta el flujo del programa, gestiona las listas en memoria y ejecuta la lógica de negocio de cada opción del menú.

Librerías: Uso del módulo nativo time para la validación de fechas reales y el cálculo matemático de días restantes entre el día actual y el vencimiento.

Interfaz Visual: Uso de secuencias de escape ANSI para aplicar colores en la consola (verde para éxitos, rojo para errores y vencimientos), mejorando la experiencia del usuario (UX).

Equipo de Desarrollo
Santiago Perozzi

Franco Estevez

Gael Conde
