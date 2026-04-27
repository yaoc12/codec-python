# Este programa calcula el Índice de Masa Corporal (IMC) y lo clasifica.

# Solicitar el peso en kg
peso = float(input("Ingrese su peso en kg: "))

# Solicitar la altura en metros
altura = float(input("Ingrese su altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Clasificar el IMC
if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")

##Lógica condicional con if, elif y else para calcular el Índice de Masa Corporal (IMC) de una persona a partir de su peso y altura ingresados por el usuario. El programa clasifica el IMC en categorías como bajo peso, normal, sobrepeso u obesidad, y muestra el resultado al final.