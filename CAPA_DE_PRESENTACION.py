#Desarrollar un programa en Python que permita registrar información básica
# de estudiantes y determinar su estado académico utilizando una estructur
# organizada por capas.

from cal_promedio import cal_promedio, deter_estado

estudiante = []

def regis_estudiante():
    nombre = input("Ingrese el nombre del estudiante: ")
    mota1 = float(input("Ingrese la primera mota del estudiante: "))
    nota2 = float(input("Ingrese la segunda mota del estudiante: "))
    nota3 = float(input("Ingrese la tercera mota del estudiante: "))

    promedio = cal_promedio(nota1,nota2,nota3)
    estado = deter_estado(promedio)

    estudiante = {
        "nombre": nombre,
        promedio: promedio,
        estado: estado
    }
    estudiante.append(estudiante)

    print("estudiante registrado correctamente")

def mostrar_estudiante():

        if len(estudiante) == 0:
            print("No hay estudiantes registrados\n")
        else:
            print("\n*** LISTA DE ESTUDIANTES ***\n")

            for est in estudiante:
                print("nombre:",  est["nombre"])
                print("promedio:", round(est["promedio"], 2))
                print("estado:", est["estado"])
                print("******************************")