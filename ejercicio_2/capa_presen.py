#Desarrollar un programa en Python que permita registrar información básica
# de estudiantes y determinar su estado académico utilizando una estructur
# organizada por capas.

from infor_academica.capa_domi import cal_promedio, deter_estado

estudiantes = []

def regis_estudiante():
    nombre = input("Ingrese el nombre: ")
    nota1 = float(input("Ingrese nota 1: "))
    nota2 = float(input("Ingrese nota 2: "))
    nota3 = float(input("Ingrese nota 3: "))

    promedio = cal_promedio(nota1, nota2, nota3)
    estado = deter_estado(promedio)

    estudiante = {
        "nombre": nombre,
        "promedio": promedio,
        "estado": estado
    }

    estudiantes.append(estudiante)

    print("Estudiante registrado correctamente")


def mostrar_estudiante():
    if len(estudiantes) == 0:
        print("No hay estudiantes registrados\n")
    else:
        print("\n*** LISTA DE ESTUDIANTES ***\n")

        for est in estudiantes:
            print("---------------******---------------")
            print("nombre:", est["nombre"])
            print("promedio:", round(est["promedio"], 2))
            print("estado:", est["estado"])
            print("---------------******---------------")

#MANUEL MORENO