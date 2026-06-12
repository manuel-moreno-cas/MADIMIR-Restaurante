#solicite una lista de 10 numeros y genera una nueva lista que contenga los
# numeros sin repetir

numeros = []

for i in range(10):
    numero = int(input(f"ingrese el numero{i+1}:"))
    numeros.append(numero)

    numeros_sin_repetir = []
    for numero in numeros:
        if numero not in numeros_sin_repetir:
            numeros_sin_repetir.append(numero)

print("\n lista original", numeros)
print("lista sin numeros repetidos", numeros_sin_repetir)
