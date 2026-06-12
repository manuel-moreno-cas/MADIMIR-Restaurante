#crea un programa que permita controlar la venta de pasajes de una empresa de transporte
#urbano el programa debe pedir acceso al usuario por un numero de identificacion y contraseña
# el programa ademas debe calcular el costo de los tikets que se vende
#teniendo en cuenta lo siguiente reglas: menores de 5 años gratis, de 5 a 18 años tarifa
#estuduantil, costo 2 mil, de 19 a 60 años tarifa full costo 3200, para mayores de 60 años
#tarifa mayor tiene un descuento del 40 % a la tarifa full
print("\n----- EMPRESA DE TRANSPORTE MANUEXPREX-----\n")

usua = input("Ingrese su usuario: ")
contra = input("ingrese su contraseña: ")

print("\n------usuario y contraseña registrados correctamente------\n")

nombre = input("ingrese su nombre: ")
edad = int(input("ingrese su edad: "))
cantidad = int(input("ingrese su cantidad: "))

if edad <5:
    tipo = "gratis"
    costo = 0
elif edad <= 18:
    tipo = "estudiantil"
    costo = 2000
elif edad <= 60:
    tipo = "full"
    costo = 3200
else:
    tipo = "adulto mayor (40% descuento)"
    costo = int(3200*0.40)

pago_total = costo * cantidad

print("\n----- FACTURA DE PAGO -----\n")
print("usuario: ",usua)
print("nombre pasajero: ",nombre)
print("edad: ",edad)
print("tipo de ticket: ",tipo)
print("cantidad de tickets comprados: ",cantidad)
print("valor a pagar: $",costo)
print("valor a pagar: $",pago_total)
print("\n------ GRACIAS POR SU COMPRA -----\n")

#MANUEL MORENO



