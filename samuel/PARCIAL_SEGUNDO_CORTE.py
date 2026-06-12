# CREA UN PROGRAMA QUE MUESTRE LAS SIGUIENTES OPCIONES:
# 1. SUMAR NUMERO
# 2. MOSTRAR TABLA DE MULTIPLICAR
# 3. VERIFICAR NUMERO PAR O IMPAR
# 4. VERIFICAR NUMEROS POSITIVOS Y NEGATIVOS
# 5. SALIR
# EL PROGRAMA EL MENU SIEMPRE DEBE ESTAR REPITIENDOSE Y TERMINAR SOLO CUANDO EL USUARIO ELIJA
# SALIR, EN LA OPCION DE LA TABLA DE MULTIPLICAR DEBE PEDIR EL NUMERO DE LA TABLA Y CALCULARLA
# HASTA EL 10, EN LA OPCION 4 SE DEBE IR PIDIENDO DIFERENTES NUMEROS EL CUAL SE DEBE DETENER
# CUANDO SE ESCRIBA CERO, DEBE MOSTRAR CUALES Y CUANTOS SON POSITIVOS Y CUALES Y CUANTOS SON
# NEGATIVOS

while True:
    print("\n ***** MENU *****\n")
    print("1. sumar numeros")
    print("2. tabla de multiplicar numeros")
    print("3. numero par o impar")
    print("4. numeros positivos o negativos")
    print("5. salir")

    opcion = input("PORFAVOR ESCOJA UNA OPCION:")

    if opcion == "1":
        a = float(input("ingrese primer numero: "))
        b = float(input("ingrese segundo numero: "))
        print("SU RESULTADO ES:", a+b)

    elif opcion == "2":
        num = int(input("INGRESE EL NUMERO DE LA TABLA QUE DESEE SABER: "))
        for i in range(1,11):
            print(num,"x",i,"=",num*i)

    elif opcion == "3":
        num  = int(input("POR FAVOR INGRESE UN NUMERO: "))
        if num%2 == 0:
            print("SU NUMERO ES PAR...")
        else:
            print("SU NUMERO ES IMPAR...")

    elif opcion == "4":
        positivo = 0
        negativo = 0
        while True:
            num = float(input("PORFAVOR INGRESE UN NUMERO: "))
            if num == 0:
                break
            elif num > 0:
                positivo += 1
            else:
                negativo += 1

        print("los numeros positivos son: ", positivo)
        print("los numeros negativos son: ", negativo)

    elif opcion == "5":
        print("\n**** saliendo del programa... *****\n")
        break

    else:
        print("Opcion invalida")

# MANUEL MORENO CASTRO
