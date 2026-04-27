# Este programa calcula la suma de los primeros N números naturales.

# Solicitar el número N
N = int(input("Ingrese un número: "))

# Inicializar la suma en 0
suma = 0

# Bucle for para sumar desde 1 hasta N
for i in range(1, N+1):
    # Agregar i a la suma
    suma += i

# Imprimir el resultado
print(f"La suma es {suma}")

##Bucle for para calcular la suma de los primeros N números enteros, donde N es un número positivo ingresado por el usuario. El resultado se muestra al final.
