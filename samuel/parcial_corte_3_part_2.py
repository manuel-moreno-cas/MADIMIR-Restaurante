# tienda virtual

productos = ["portatil", "mouse", "teclado", "monitor"
]
categorias = {"tecnologias", "accesorios", "perifericos"}

inventario = {
    "portatil": (2500000, 5),
    "mouse": (50000, 10),
    "teclado": (120000, 8),
    "monitor": (80000, 3),
}
print("********** TIENDA VIRTUAL **********")
print("\nPRODUCTOS DISPONIBLES:")
for producto in productos:
    print(producto)

print("\nCATEGORIAS:")
for categoria in categorias:
    print(categoria)

buscar = input("\ningrese el nombre del producto que desea consultar: ")

if buscar in inventario:
    precio, cantidad = inventario[buscar]

    print("\nproducto encontrado")
    print("precio: $", precio)
    print("cantidad disponibles: ", cantidad)

    if cantidad > 0:
        print("estado:  disponible")
    else:
        print("estado:  agotado")
else:
    print("\nel producto no existe en la tienda.")

# manuel moreno