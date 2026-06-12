# crea un programa que lea un numero y muestre como resultado su tabla de multiplicacion
# hasta el numero 12
num= int(input("Ingresa un número: "))

print(f"\nTabla de multiplicar del {num}:\n")

for i in range(1, 13):
    resul = num * i
    print(f"{num} x {i} = {resul}")

# MANUEL MORENO

