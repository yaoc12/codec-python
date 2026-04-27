# Este programa calcula el descuento en una compra según el monto total.

# Solicitar el total de la compra
compra = float(input("Ingrese el total de la compra: "))

# Determinar el descuento basado en el monto
if compra < 50:
    # Sin descuento para compras menores a 50
    descuento = 0
elif compra <= 100:
    # 5% de descuento para compras entre 50 y 100
    descuento = 0.05
else:
    # 10% de descuento para compras mayores a 100
    descuento = 0.10

# Calcular el total a pagar aplicando el descuento
total = compra - (compra * descuento)

# Mostrar el total a pagar con dos decimales
print(f"Total a pagar: ${total:.2f}")

##Lógica condicional con if, elif y else para aplicar un descuento en una tienda según el monto de la compra ingresado por el usuario. El descuento se aplica de la siguiente manera: si la compra es menor a $50, no hay descuento; si la compra está entre $50 y $100, se aplica un 5% de descuento; y si la compra es mayor a $100, se aplica un 10% de descuento. El total a pagar se muestra al final.