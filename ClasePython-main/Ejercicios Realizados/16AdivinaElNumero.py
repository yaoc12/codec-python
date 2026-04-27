# Este programa es un juego para adivinar un número aleatorio.

# Importar el módulo random para generar números aleatorios
import random

# Generar un número secreto entre 1 y 20
secreto = random.randint(1, 20)

# Definir el número de intentos
intentos = 5

# Bucle for para los intentos
for i in range(intentos):
    # Solicitar un número al usuario
    num = int(input("Adivina el número (1-20): "))
    # Verificar si es correcto
    if num == secreto:
        print("¡Correcto!")
        # Salir del bucle
        break
    elif num < secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
else:
    # Si no adivinó en los intentos, mostrar el número
    print(f"Se acabaron los intentos. El número era {secreto}.")

##Bucle for para implementar un juego de adivinar el número. El programa genera un número aleatorio entre 1 y 20, y el usuario tiene 5 intentos para adivinarlo. En cada intento, el programa indica si el número ingresado es correcto, mayor o menor que el número secreto. Si el usuario adivina correctamente, se muestra un mensaje de felicitación; si se agotan los intentos sin adivinar, se revela el número secreto.