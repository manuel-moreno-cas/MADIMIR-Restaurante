# crea un programa que evalue el valor total de una compra y aplique los descuentos
# deacuerdo a la siguiente informacion: si es menor de 5 mil no tiene descuento
# si es mas de 5 mil 10% de descuento, para compras superiores a 20 mil 20% descuento

producto = input("Ingrese el producto que desea pagar: ")
valor_compra = float(input("Ingrese el valor del producto : "))

descuento = 0
total_pagar = 0

if valor_compra < 5000:
    descuento = 0
elif valor_compra >= 5000 and valor_compra <= 20000:
    descuento = valor_compra * 0.10
else:
    descuento = valor_compra * 0.20

total_pagar = valor_compra - descuento

print("\n--------- FACTURA DE COMPRA ---------")
print("producto: ",producto)
print("Valor de la compra:", valor_compra)
print("Descuento aplicado:", descuento)
print("Total a pagar:", total_pagar)
print("\n---------- GRACIAS POR SU COMPRA ----------")

# MANUEL MORENO
