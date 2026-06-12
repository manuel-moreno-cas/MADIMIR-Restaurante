#Desarrollar un programa en Python que permita registrar información básica
# de estudiantes y determinar su estado académico utilizando una estructur
# organizada por capas.

from infor_academica.capa_presen import regis_estudiante,mostrar_estudiante
#from infor_academica.capa_presen import cal_promedio,deter_estado
def menu():
    opc = 0

    while opc != 3:

        print("\n*** SISTEMAS DE ESTUDIANTES ***")
        print("1. Registrar estudiantes")
        print("2. Mostrar estudiantes")
        print("3. Salir")

        opc = int(input("Ingrese su opcion: "))

        if opc == 1:
            regis_estudiante()

        elif opc == 2:
            mostrar_estudiante()

        elif opc == 3:
            print("Saliendo del sistema.....")
        else:
            print("Opcion no valida")

menu()

# MANUEL MORENO