def regis_usuario():
    listausuarios =[]

    while True:
        print("\n----- REGISTROS DE USUARIOS -----")
        nombre = input("ingrese su usuario: ")

        print("seleccione su tipo de menbresia:")
        print("1. basica")
        print("2. premium")
        print("3. vip")

        opcion = (input("Digite su opcion: "))
        if opcion == "1":
            resultado = "BASICA"
            print("su menbresia es: ", resultado)
            costo = 50000
            print("\n costo: ", costo)
        elif opcion == "2":
            resultado = "PREMIUM"
            print("su menbresia es: ", resultado)
            costo = 80000
            print("\n costo: ", costo)
        elif opcion == "3":
            resultado = "VIP"
            print("su menbresia es: ", resultado)
            costo = 120000
            print("\n costo: ", costo)
        else:
            print("opcion invalida")
            continue

        usuario ={
            "nombre":nombre,
            "resultado":resultado,
            "costo":costo
        }
        listausuarios.append(usuario)

        print("usuarios rejistrados correctamente")

        continuar = input("¿desea continuar? (s/n): ").lower()
        if continuar != "s":
            break


    print("\n----- REPORTE _____\n")
    for i,u in enumerate(listausuarios,start=1):
        print(f"{i}. {u['nombre']}")
        print(f"{i}. {u['resultado']}")
        print(f"{i}. {u['costo']}")

regis_usuario()






