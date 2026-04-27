# Este programa simula una caja registradora que calcula el total con descuento.

# Inicializar total en 0
total = 0

# Bucle while para ingresar precios hasta que se ingrese 0
while True:
    # Solicitar precio del producto
    precio = float(input("Ingrese precio del producto (0 para terminar): "))
    # Si precio es 0, salir del bucle
    if precio == 0:
        break
    # Agregar precio al total
    total += precio

# Aplicar descuento si total > 100
if total > 100:
    total *= 0.9

# Mostrar el total a pagar
print(f"Total a pagar: ${total:.2f}")

##Bucle while para simular una caja registradora. El programa solicita al usuario que ingrese el precio de cada producto, sumando el total hasta que el usuario ingrese 0 para finalizar la compra. Si el total supera los $100, se aplica un descuento del 10%. Finalmente, se muestra el total a pagar con dos decimales.