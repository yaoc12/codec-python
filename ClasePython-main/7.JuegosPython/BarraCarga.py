'''
Enunciado del Ejercicio: Simulador de Carga de Archivos

Contexto: En el desarrollo de aplicaciones web y de escritorio, es vital informar al usuario sobre el progreso de tareas 
que no son instantáneas, como la subida de un archivo a la nube. Tu objetivo es programar un codigo que simule visualmente 
este proceso en la consola.

Instrucciones

Escribe un programa en Python (o el lenguaje de tu preferencia) que realice las siguientes acciones:

	1.	Entrada de datos:
•	Solicitar al usuario el tamaño total del archivo (en Megabytes).
•	Solicitar al usuario el tiempo total de subida deseado (en segundos).
	2.	Lógica de simulación:
•	El programa debe calcular cuánto tiempo debe pasar para que la barra aumente su progreso (puedes usar intervalos de 1% o 10%).
•	Utilizar un bucle para representar el paso del tiempo y el aumento del porcentaje.
	3.	Interfaz visual (Consola):
•	Mostrar una barra de progreso que se llene dinámicamente usando caracteres (por ejemplo: [##########..........]).
•	Mostrar el porcentaje actual al lado de la barra (ej: 50%).
•	Al finalizar, el programa debe mostrar un mensaje de "Carga Completa" con el tamaño del archivo procesado.

Ejemplo de Salida Esperada
Ingrese el tamaño del archivo (MB): 100
Ingrese el tiempo de carga (segundos): 5

Iniciando subida de 100 MB...
[#####---------------] 25%
[##########----------] 50%
[###############-----] 75%
[####################] 100%

¡Archivo de 100 MB subido con éxito!

Tips de Lógica para el Estudiante (Opcional)
•	Matemática simple: Si el tiempo total es T y quieres actualizar la barra 20 veces (de 5% en 5%), cada pausa debe ser de T/20 segundos.
•	Librerías sugeridas: En Python, puedes usar time.sleep() para las pausas y el carácter especial \r (retorno de carro) para que la barra se actualice en la misma línea en lugar de imprimir una nueva cada vez.

Solución del Ejercicio Propuesto 
'''


import time  # Librería para pausar la ejecución con time.sleep()

# ----- 1. Encabezado visual -----
print("=" * 60)
print("   Simulador de Carga de Archivos   ".center(60))
print("=" * 60)

# ----- 2. Entrada de datos -----
# Pedimos los valores al usuario y los convertimos a enteros.
# El programa espera que se ingrese un número válido.
tamaño = int(input("Ingrese el tamaño del archivo (MB): "))
tiempo_total = int(input("Ingrese el tiempo de carga (segundos): "))

print(f"\nIniciando subida de {tamaño} MB...\n")

# ----- 3. Configuración de la barra de progreso -----
pasos = 20  # Número de actualizaciones de la barra (20 pasos = 5% por paso)
pausa = tiempo_total / pasos  # Segundos entre cada actualización de progreso

# ----- 4. Simulación del progreso -----
# El bucle recorre los pasos de 1 a 20 para construir la barra.
for i in range(1, pasos + 1):
    porcentaje = int((i / pasos) * 100)  # Convierte el paso actual a porcentaje
    barra = "#" * i + "-" * (pasos - i)  # Construye la barra visual

    # Muestra la barra en la misma línea y fuerza el refresco inmediato.
    print(f"\r[{barra}] {porcentaje}%", end="", flush=True)

    time.sleep(pausa)  # Pausa antes del siguiente paso

# Avanza a la siguiente línea después de terminar la barra.
print()

# ----- 5. Mensaje final -----
print("¡Archivo de", tamaño, "MB subido con éxito!")
print("=" * 60)

'''
Explicación de la Lógica Clave:

• pasos = 20: define cuántas veces se actualiza la barra.
Cada paso equivale a un 5% de avance.
• pausa = tiempo_total / pasos: calcula cuánto tiempo debe esperar
el programa entre cada actualización.
• El bucle for simula el avance de la carga a través del tiempo.
• porcentaje = int((i / pasos) * 100): convierte el paso actual
en un porcentaje de 0 a 100.
• barra = "#" * i + "-" * (pasos - i): construye la barra
con caracteres llenos y vacíos.
• print(..., end="", flush=True): actualiza la barra en la misma línea.
• time.sleep(pausa): simula el tiempo de carga entre cada paso.

La logica clave es:

1. Entrada de datos: se solicita el tamaño del archivo y el tiempo total de carga.
2. Cálculo del intervalo: el tiempo total se divide en pasos iguales
para que el avance sea uniforme.
3. Actualización de la barra: cada iteración del bucle añade
un símbolo '#' más a la barra.
4. Visualización en la misma línea: se usa '\r' para sobreescribir
la línea actual y mostrar el progreso de izquierda a derecha.
5. Mensaje final: al terminar el bucle, se muestra que la carga
se completó exitosamente.
'''

