# crea un programa que simule el funcionamiento de un cajero automatico el menu de control debe tener las siguientes
# opciones, 1 consulta de saldo, 2 consignaciones, 3 retios, 4 salida, el menu siempre debe
# estar activo el programa solo termina cuando el usuario desea salir.
saldo = 0

while True:
    print("\n--- CAJERO AUTOMATICO ---")
    print("1. Consultar saldo")
    print("2. Consignar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print(f"\nTu saldo actual es: ${saldo}")

    elif opcion == "2":
        consignacion = float(input("Ingresa el valor a consignar: "))

        if consignacion > 0:
            saldo += consignacion
            print(f"Consignación exitosa. Nuevo saldo: ${saldo}")
        else:
            print("Valor inválido.")

    elif opcion == "3":
        retiro = float(input("Ingresa el valor a retirar: "))

        if retiro > 0 and retiro <= saldo:
            saldo -= retiro
            print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
        else:
            print("Fondos insuficientes o valor inválido.")

    elif opcion == "4":
        print("Gracias por usar el cajero. ¡Hasta luego!")
        break

    else:
        print("Opción inválida, intenta nuevamente.")