#crea un programa que alamacene los datos de una vaca de una finca
#los animales se identifican por codigos y por cada vaca se debe mostrar
#el nombre la raza la edad y cantidad en leche y peso se debe mostrar los datos de cada animal
print("\n****** DATOS DE LA VACA *****\n")

codigo = input("Ingrese el codigo de la vaca: ")
nombre = input("Ingrese el nombre de la vaca: ")
raza = input("Ingrese la raza: ")
edad = int(input("Ingrese la edad de la vaca: "))
leche = float(input("Ingrese la cantidad de leche producida: "))
peso = float(input("Ingrese el peso de la vaca: "))

print("\n***** INFORMACION DEL ANIMAL *****\n")
print("Codigo:", codigo)
print("Nombre:", nombre)
print("Raza:", raza)
print("Edad:", edad, "años")
print("Cantidad de leche:", leche, "litros")
print("Peso:", peso, "kg")

# MANUEL MORENO