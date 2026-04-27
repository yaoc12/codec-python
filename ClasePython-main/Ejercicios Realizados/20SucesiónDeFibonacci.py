# Este programa genera los primeros N términos de la sucesión de Fibonacci.

# Solicitar el número de términos
n = int(input("¿Cuántos términos de Fibonacci desea? "))

# Inicializar los primeros dos términos
a, b = 0, 1

# Bucle for para generar n términos
for i in range(n):
    # Imprimir el término actual
    print(a, end=" ")
    # Actualizar a y b para el siguiente término
    a, b = b, a + b

##Bucle for para generar los primeros N términos de la sucesión de Fibonacci, donde N es un número entero positivo ingresado por el usuario. El programa utiliza dos variables para almacenar los términos actuales de la sucesión y actualiza estos valores en cada iteración del bucle, imprimiendo cada término en la misma línea separado por un espacio.
