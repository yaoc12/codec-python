# Este programa clasifica un número como positivo, negativo o cero.

# Solicitar un número al usuario
num = int(input("Ingrese un número: "))

# Verificar si el número es positivo
if num > 0:
    print("El número es positivo.")
# Verificar si el número es negativo
elif num < 0:
    print("El número es negativo.")
# Si no es positivo ni negativo, es cero
else:
    print("El número es cero.")

##Lógica condicional con if, elif y else para determinar si un número ingresado por el usuario es positivo, negativo o cero. El resultado se muestra al final.