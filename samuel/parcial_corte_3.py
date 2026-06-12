# SISTEMA DE BIBLIOTECA
libros = [
    "cien años de soledad",
    "donquijote de la mancha",
    "el principito"
]

categorias = {
    "novela",
    "aventura",
    "fantasia",
}

autor = ("gabriel gacias marquez",)
menbresia = ("estudiante",)
nacionalidad = ("colombiana",)

disponibles = {
    "cien años de soledad":5,
    "don quijote de la mancha":3,
    "el principito":7
}

usuario = []
continuar = ("s")

while continuar.lower() == "s":
    nombre = input("Ingrese su nombre: ")
    usuario.append(nombre)
    continuar = input("¿ desea registrar otro usuario? (s/n): ")

print("********** SISTEMA DE BIBLIOTECA **********")

print("\n usuarios registrados:")
for usuario in usuario:
    print(usuario)
    
print("\n libros registados:")
for libro in libros:
    print(libro)

print("\n categorias disponibles:")
for categoria in categorias:
    print(categoria)

print("\n informacion del usuario:")
print("autor favorito:", autor[0])
print("tipo de menbresia:", menbresia[0])
print("nacionalidad:", nacionalidad[0])

print("\n cantidad de libros disponibles:")
for libros, cantidad in disponibles.items():
    print(libros, "->", cantidad, "ejemplares")

# manuel moreno