# cree un programa que solicite al usuario cinco calificaciones, almacene en una lista
#y calcule el promedio

notas_estudiantes = []

for contador_notas in range(5):
    nota_ingresada = float(input(f"digite la nota{contador_notas +1}:"))
    notas_estudiantes.append(nota_ingresada)

promedio_final = sum(notas_estudiantes)/5

print("\n notas almacenadas:",notas_estudiantes)
print("el promedio de las notas es:", promedio_final)

