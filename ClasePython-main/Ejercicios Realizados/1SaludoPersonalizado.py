# Este programa solicita el nombre y la edad del usuario, calcula su año de nacimiento aproximado y muestra un saludo personalizado.

# Solicitar el nombre del usuario
nombre = input("¿Cuál es tu nombre? ")

# Solicitar la edad del usuario y convertir la entrada a un número entero
edad = int(input("¿Cuántos años tienes? "))

# Definir el año actual (puedes actualizar este valor según el año en curso)
año_actual = 2026

# Calcular el año de nacimiento restando la edad del usuario al año actual
año_nacimiento = año_actual - edad

# Mostrar un mensaje de saludo que incluye el nombre del usuario y su año de nacimiento aproximado
print(f"Hola {nombre}, bienvenido/a. Naciste aproximadamente en {año_nacimiento}.")

##Ejercicio para crear un saludo personalizado que incluye el nombre del usuario y calcula su año de nacimiento a partir de su edad ingresada.