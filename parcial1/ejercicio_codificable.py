alquileres = []
cantidad = int(input("¿Cuántos alquileres va a registrar? "))

for i in range(cantidad):
    dias = int(input(f"Ingrese los días del alquiler {i+1}: "))
    alquileres.append(dias)


def calcular_reporte_alquileres(alquileres):
    total_alquileres = 0
    cortos = 0
    extendidos = 0
    total_dias = 0

    for dias in alquileres:
        total_alquileres += 1
        total_dias += dias

        if 1 <= dias <= 3:
            cortos += 1
        else:
            extendidos += 1

    if total_alquileres > 0:
        promedio_dias = total_dias / total_alquileres
        porcentaje_cortos = (cortos / total_alquileres) * 100
        porcentaje_extendidos = (extendidos / total_alquileres) * 100
    else:
        promedio_dias = 0
        porcentaje_cortos = 0
        porcentaje_extendidos = 0

    print("\n----- REPORTE DEL DÍA -----")
    print("Total alquileres:", total_alquileres)
    print("Alquileres cortos:", cortos)
    print("Alquileres extendidos:", extendidos)
    print("Total de días:", total_dias)
    print("Promedio de días:", round(promedio_dias, 2))
    print("Porcentaje cortos:", round(porcentaje_cortos, 2), "%")
    print("Porcentaje extendidos:", round(porcentaje_extendidos, 2), "%")


calcular_reporte_alquileres(alquileres)

# manuel moreno