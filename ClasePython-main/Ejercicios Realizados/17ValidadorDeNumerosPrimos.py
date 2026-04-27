# Este programa verifica si un número es primo.

# Solicitar el número al usuario
num = int(input("Ingrese un número: "))

# Asumir que es primo inicialmente
es_primo = True

# Verificar si es menor o igual a 1
if num <= 1:
    es_primo = False
else:
    # Bucle for para verificar divisores desde 2 hasta num-1
    for i in range(2, num):
        # Si es divisible, no es primo
        if num % i == 0:
            es_primo = False
            # Salir del bucle
            break

# Mostrar el resultado
if es_primo:
    print("Es primo.")
else:
    print("No es primo.")

##Bucle for para determinar si un número entero ingresado por el usuario es primo o no. El programa verifica si el número es menor o igual a 1 (en cuyo caso no es primo) y luego itera desde 2 hasta el número menos uno para verificar si el número es divisible por algún otro número. Si encuentra un divisor, marca el número como no primo y sale del bucle. Al final, se muestra un mensaje indicando si el número es primo o no.