'''
Enunciado del Ejercicio: Geometría con Bucles (Arte ASCII)

Objetivo: Desarrollar la lógica de programación y el manejo de bucles anidados (for o while) para representar figuras 
geométricas bidimensionales en la terminal utilizando caracteres (como *, + o #).

Descripción de la Tarea

Debes crear un programa que, al ejecutarse, imprima de forma clara las siguientes cinco figuras. El usuario debería poder 
definir el tamaño (lado, radio o altura) de las figuras antes de imprimirlas.

Figuras Requeridas:
1.Triángulo Rectángulo: El programa debe imprimir un triángulo alineado a la izquierda.
2.Cuadrado: Una representación con la misma cantidad de filas y columnas.
3.Rectángulo: Donde la base sea visiblemente mayor a la altura (ejemplo: proporción 2:1).
4.Círculo: (Reto de lógica) Utiliza la ecuación del círculo o una aproximación de distancia de puntos para dibujar 
        una forma redondeada.
5.Pentágono: Una figura de 5 lados (puedes combinar un triángulo sobre un trapecio o rectángulo).

Requerimientos Técnicos
•Visualización: Crear un menú que permita elegir la figura a imprimir.
•Interactividad: El programa debe preguntar al usuario: "Ingrese el tamaño para sus figuras:.".
•Estructura: Utiliza bucles anidados. El bucle externo controlará las filas (eje Y) y el interno las columnas (eje X).
•Presentación: Cada figura debe estar separada por un título y un espacio en blanco para que sea legible.

Ejemplo de Salida Esperada (Tamaño 5)

--- CUADRADO ---
# # # # #
# # # # #
# # # # #
# # # # #
# # # # #

--- RECTÁNGULO (5x10) ---
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # #

--- TRIÁNGULO ---
# 
# # 
# # # 
# # # # 
# # # # #

--- CÍRCULO (Radio 5) ---
      # # # #      
    # # # # # #    
  # # # # # # # #  
  # # # # # # # #  
    # # # # # #    
      # # # #      

--- PENTÁGONO ---
      #      
    # # #    
  # # # # #  
  # # # # #  
  # # # # #  

Solución del Ejercicio Propuesto
'''

# Importación de módulos necesarios
import math  # Importar math por si se desea usar funciones matemáticas adicionales en figuras complejas
import time  # Importar time para pausar el programa y dar tiempo de lectura al usuario

# Encabezado visual del programa
print("=" * 60)
print("   Arte ASCII con Figuras Geométricas   ".center(60))
print("=" * 60)

# Muestra el menú de opciones para que el usuario elija la figura
print("Seleccione la figura que desea imprimir:")
print("1. Triángulo Rectángulo")
print("2. Cuadrado")
print("3. Rectángulo")
print("4. Círculo")
print("5. Pentágono")
print("6. Salir")

# Bucle principal del programa: se repite hasta que el usuario elige salir
while True:
    opcion = input("\nIngrese el número de la figura: ")

    # Permite terminar el programa cuando el usuario ingresa la opción 6
    if opcion == "6":
        print("Has salido del programa. ¡Hasta pronto!")
        break

    # Pide el tamaño de la figura elegida y lo convierte en número entero
    tamaño = int(input("Ingrese el tamaño para su figura: "))
    print()

    # --- TRIÁNGULO RECTÁNGULO ---
    if opcion == "1":
        print("--- TRIÁNGULO RECTÁNGULO ---")
        for i in range(1, tamaño + 1):
            # Imprime una fila con i símbolos '# ' para crear el triángulo alineado a la izquierda
            print("# " * i)

    # --- CUADRADO ---
    elif opcion == "2":
        print("--- CUADRADO ---")
        for i in range(tamaño):
            # Imprime una fila con tamaño símbolos para formar cuadrado de lado = tamaño
            print("# " * tamaño)

    # --- RECTÁNGULO ---
    elif opcion == "3":
        print(f"--- RECTÁNGULO ({tamaño}x{tamaño*2}) ---")
        for i in range(tamaño):
            # Usa el doble de columnas que de filas para un rectángulo ancho
            print("# " * (tamaño * 2))

    # --- CÍRCULO ---
    elif opcion == "4":
        print(f"--- CÍRCULO (Radio {tamaño}) ---")
        for y in range(-tamaño, tamaño + 1):
            fila = ""
            for x in range(-tamaño, tamaño + 1):
                # Comprueba si el punto (x, y) está dentro del círculo de radio tamaño
                if x*x + y*y <= tamaño*tamaño:
                    fila += "# "
                else:
                    fila += "  "
            print(fila)

    # --- PENTÁGONO ---
    elif opcion == "5":
        print("--- PENTÁGONO ---")
        # Parte superior en forma de triángulo para dar el vértice superior
        for i in range(1, tamaño):
            print(" " * (tamaño - i) + "# " * i)
        # Parte inferior como una base ancha de tamaño filas
        for i in range(tamaño):
            print("# " * tamaño)

    # Opción inválida cuando el usuario no ingresa un número del 1 al 6
    else:
        print("Opción inválida. Intente nuevamente.")

    # Pausa breve para que el usuario vea el resultado antes de continuar
    time.sleep(1)
    print("\n" + "=" * 60)

'''
Explicación de la Lógica Clave:

• El programa muestra un menú con las figuras disponibles y espera la opción del usuario.
• La opción "6" cierra el programa con un mensaje de despedida.
• Para cualquier otra figura, se pide un tamaño entero que controla la cantidad de filas y columnas.
• Triángulo rectángulo: se imprime una fila más larga en cada iteración, creando una forma triangular.
• Cuadrado: se imprime el mismo número de símbolos "#" en cada fila, manteniendo filas y columnas iguales.
• Rectángulo: se usa el doble de columnas que de filas para generar una figura más ancha.
• Círculo: cada punto se comprueba con la fórmula x² + y² ≤ r² para determinar si está dentro del radio.
• Pentágono: combina una parte superior en triángulo con una base rectangular para aproximar la forma.
• while True: mantiene el programa ejecutándose hasta que el usuario elige salir.
• time.sleep(1): añade una pausa visual entre un dibujo y el siguiente para mejorar la lectura.

La lógica clave es:

1) mostrar el menú,
2) leer la opción del usuario,
3) pedir el tamaño deseado,
4) usar bucles para dibujar la figura fila por fila,
5) validar la entrada y repetir hasta que el usuario decida salir.
'''