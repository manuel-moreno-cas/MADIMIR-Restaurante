#Cree una función que reciba tres números y retorne el mayor de ellos.
def mayor_de_tres(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

resultado = mayor_de_tres(num1, num2, num3)

print("El número mayor es:", resultado)

print("\n*** FIN DEL EJERCICIO ***")
print("\n*** GRACIAS ***")

#MANUEL MORENO