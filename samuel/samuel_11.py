# crea un programa que pida dos muneros y pida realizar la operacion que desea ejecutar
# use condicionales para realizar la operacion correcta
num1 = float(input("Digite su primer numero: "))
num2 = float(input("Digite su segundo numero: "))

print(" seleccione la operacion que gusta realizar:")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")

opcion = (input("Elige su opcion: "))
if opcion == "1":
    resultado = num1 + num2
    print("El resultado es: ", resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("El resultado es: ", resultado)
elif opcion == "3":
    resultado = num1 * num2
    print("El resultado es: ", resultado)
elif opcion == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado es: ", resultado)
    else:
        resultado = 0
        print("\n--- ERROR --- ")
        print("no se puede dividir entre cero")
else:
    print("Opcion no valida")

# MANUEL MORENO