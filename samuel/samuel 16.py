# escriba un programa que simule un menu de selecciones, si el usuario dice y o si
# debe continuar con un mensaje de bienvenida si dice n o no debe salir del programa y un mensaje de
# despedida, si dice cualquier otra cosa debe repetir la posibilidad de repetir nuevamente la
# opcion
NUMERA = float(input("Ingresa el número a dividir (numerador): "))

while True:
    DEMO = float(input("Ingresa el número por el que vas a dividir (denominador): "))

    if DEMO != 0:
        break
    else:
        print("Error: NO ES DIVICIBLE ENTRE 0 INGRESE UN NUMERO NUEVAMENTE:\n")

RESUL = NUMERA / DEMO

print(f"\nEl resultado de la división es: {RESUL}")
# MANUEL MORENO
