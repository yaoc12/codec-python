# Este programa determina si se aprueba un crédito basado en salario y deudas.

# Solicitar el salario mensual
salario = float(input("Ingrese su salario mensual: "))

# Solicitar si tiene deudas, convertir a minúsculas
deuda = input("¿Tiene deudas? (sí/no): ").lower()

# Verificar condiciones para aprobar el crédito
if salario > 1000 and deuda == "no":
    # Si salario > 1000 y no tiene deudas, aprobar
    print("Crédito Aprobado")
else:
    # De lo contrario, denegar
    print("Crédito Denegado")

##Lógica condicional con if y else para determinar si un crédito es aprobado o denegado. El programa solicita al usuario que ingrese su salario mensual y si tiene deudas. El crédito se aprueba si el salario es mayor a $1000 y no tiene deudas; de lo contrario, se deniega el crédito. El resultado se muestra al final.