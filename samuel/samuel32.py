# crea un programa que pida 10 numeros enteros y luego muestre el mayor y el menor

numeros = []

for contador in range(10):
    numero = int(input(f"ingrese el numero {contador+1}: "))
    numeros.append(numero)

mayor = max(numeros)
menor = min(numeros)

print("\n lista de numeros:", numeros)
print("el numero mayor es:", mayor)
print("el numero menor es:", menor)