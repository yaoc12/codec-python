# Este programa compara dos números enteros y determina cuál es mayor.

# Solicitar el primer número entero
a = int(input("Ingrese el primer número: "))

# Solicitar el segundo número entero
b = int(input("Ingrese el segundo número: "))

# Comparar los dos números
if a > b:
    # Si a es mayor que b, imprimir a como el mayor
    print(f"El mayor es {a}")
else:
    # Si b es mayor o igual a a, imprimir b como el mayor (nota: no maneja empate explícitamente)
    print(f"El mayor es {b}")

##Lógica condicional con if y else para determinar cuál de dos números enteros ingresados por el usuario es mayor. El programa solicita al usuario que ingrese dos números y luego compara ambos para imprimir cuál es el mayor.