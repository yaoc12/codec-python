# Este programa realiza una cuenta regresiva desde un número dado hasta cero.

# Solicitar un número positivo
n = int(input("Ingrese un número positivo: "))

# Bucle while para contar desde n hasta 0
while n >= 0:
    # Imprimir el número actual
    print(n)
    # Decrementar n
    n -= 1

# Después del bucle, imprimir mensaje de despegue
print("¡Despegue!")

##Bucle while para crear una cuenta regresiva desde un número positivo ingresado por el usuario hasta cero, imprimiendo cada número en la cuenta regresiva. Al finalizar, se imprime un mensaje de "¡Despegue!".