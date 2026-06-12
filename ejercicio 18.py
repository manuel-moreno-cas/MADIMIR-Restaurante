#Cree una función que reciba una nota y retorne 'Aprobado' o 'Reprobado'.
def evaluar_nota(nota):
    if nota >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"

n = float(input("por favor ingre la nota: "))
resultado = evaluar_nota(n)

print(resultado)

print("\n*** FIN DEL EJERCICIO ***")
print("\n*** GRACIA ***")

#MANUEL MORENO