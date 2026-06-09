# SmartBudget Control

**Sistema de Administración Financiera Personal - Fase 1**

## Descripción del Proyecto
SmartBudget Control es una aplicación interactiva desarrollada en Python para la interfaz de línea de comandos. Su propósito es centralizar la administración y el análisis de los gastos y compromisos económicos del hogar. El sistema permite organizar formalmente obligaciones financieras tales como tarjetas de crédito, préstamos, servicios y suscripciones, facilitando la planificación económica familiar y previniendo atrasos en los pagos pendientes.

## Alcance Funcional

Esta primera fase del proyecto implementa una solución de gestión en memoria a través de un menú estructurado con las siguientes opciones:

### 1. Registrar movimiento (Alta)
Permite la incorporación de nuevos compromisos financieros al sistema. Incluye la validación de los datos de entrada: códigos alfanuméricos de un mínimo de 4 caracteres, montos mayores o iguales a cero, meses dentro del rango de 1 a 12, y categorías y estados de pago predefinidos. La información se almacena de forma sincronizada en estructuras de listas paralelas.

### 2. Eliminar movimiento (Baja)
Permite la remoción de un registro mediante la búsqueda de su código de deuda. Como regla de negocio orientada a preservar el historial financiero, la eliminación solo es procedente si el estado de pago del movimiento es estrictamente "Pagada Total".

### 3. Modificar movimiento (Modificación)
Permite la actualización interactiva de los atributos de un registro existente (detalle, categoría, montos, mes de vencimiento o estado de pago). El proceso valida cada nueva entrada por teclado y preserva el código identificador original.

### 4. Informe General
Presenta un listado ordenado y formateado de todos los movimientos registrados. El ordenamiento de las listas se realiza mediante el método de inserción aplicando un doble criterio:
* **Criterio Principal:** De forma descendente (de mayor a menor) según el monto pendiente de pago.
* **Criterio Secundario:** En caso de igualdad en los montos, se ordena de forma ascendente (alfabéticamente) según el detalle de la deuda.

## Estructura Técnica y Tecnologías
* **Lenguaje de programación:** Python 3.x
* **Estructuras de datos:** Siete listas paralelas para la gestión síncrona de los datos (`cod_deuda`, `det_deuda`, `categoría`, `monto_total`, `monton_pendiente`, `vencimiento`, `estado`).
* **Diseño de software:** Arquitectura modular que separa la lógica de validación, búsqueda y ordenamiento en un módulo de funciones independiente del flujo del programa principal.

## Equipo de Desarrollo
* Santiago Perozzi
* Franco Estevez
* Gael Conde
