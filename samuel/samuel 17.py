# crea un programa que valide la regla de la divicion para ejecutar el calculo,
# en caso de no cumplirse debe volver a pedir el numero
# validar division (no permitir dividir entre 0)

while True:
    NUM1 = float(input("Ingresa el primer número: "))
    NUM2 = float(input("Ingresa el segundo número (divisor): "))

    if NUM1 == 0:
        print("Error: no se puede dividir entre 0. Intenta nuevamente.\n")
    else:
        RESUL = NUM1 / NUM2
        print(f"\nEl resultado es: {RESUL}\n")
        break
# MANUEL MORENO