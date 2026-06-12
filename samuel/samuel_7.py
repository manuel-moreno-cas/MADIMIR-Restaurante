
producto = input("ingrese el nombre del producto:")
valor = float(input("ingrese el valor del producto:"))
cantidad = int(input("ingrese la cantidad del producto deseado:"))
iva = 0.19

total_de_iva = valor * cantidad
valor_sin_iva = total_de_iva * 0.19
iva_pagado = total_de_iva - valor_sin_iva

print("\n*** FACTURA ***")
print("Producto: ", producto)
print("cantidad: ", cantidad)
print("valor: ", valor)
print("IVA: ", valor_sin_iva)
print("subtotal: ", iva_pagado)
print("Valor total pagado: ", total_de_iva)