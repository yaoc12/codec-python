# Este programa clasifica la edad de una persona en categorías.

# Solicitar la edad del usuario
edad = int(input("Ingrese su edad: "))

# Verificar si está en el rango de niño (0-12)
if 0 <= edad <= 12:
    print("Niño")
# Verificar si está en el rango de adolescente (13-17)
elif 13 <= edad <= 17:
    print("Adolescente")
# Verificar si está en el rango de adulto (18-64)
elif 18 <= edad <= 64:
    print("Adulto")
# Si no entra en los anteriores, es adulto mayor
else:
    print("Adulto mayor")

##Logica condicional con if, elif y else para determinar la categoría de edad de una persona.