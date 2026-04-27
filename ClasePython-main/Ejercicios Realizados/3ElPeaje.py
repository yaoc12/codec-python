# Este programa verifica si una persona tiene la edad suficiente para conducir.

# Solicitar la edad del usuario y convertir a entero
edad = int(input("Ingrese su edad: "))

# Verificar si la edad es mayor o igual a 18
if edad >= 18:
    # Si tiene 18 o más, puede conducir
    print("Puedes conducir.")
else:
    # Si tiene menos de 18, no puede conducir
    print("Aún no tienes edad para conducir.")

##Lógica condicional con if y else para determinar si una persona tiene la edad suficiente para conducir. El programa solicita al usuario que ingrese su edad y luego verifica si es mayor o igual a 18 años. Si es así, se imprime un mensaje indicando que puede conducir; de lo contrario, se indica que aún no tiene edad para conducir.