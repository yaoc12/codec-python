# Este programa muestra la tabla de multiplicar de un número dado.

# Solicitar el número para la tabla
num = int(input("Ingrese un número: "))

# Bucle for para multiplicar por 1 a 10
for i in range(1, 11):
    # Imprimir la multiplicación
    print(f"{num} x {i} = {num*i}")

##Bucle for para generar la tabla de multiplicar de un número entero ingresado por el usuario. El programa imprime la multiplicación del número por los números del 1 al 10, mostrando el resultado en cada línea.