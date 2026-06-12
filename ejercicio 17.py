#Cree una función que determine si un número es par.
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

n = int(input("Introdusca el numero: "))

if es_par(n):
    print("El número es par")
else:
    print("El número es impar")

print("\n*** FIN DEL EJERCICIO ***")
print("\n*** GRACIA ***")

#MANUEL MORENO