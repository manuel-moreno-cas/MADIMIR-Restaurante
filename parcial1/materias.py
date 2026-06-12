

def calcular_promedio(calificacion_matematicas, calificacion_ciencias, calificacion_historia):
    suma_total_notas = calificacion_matematicas + calificacion_ciencias + calificacion_historia
    promedio_final_estudiante = suma_total_notas / 3
    return promedio_final_estudiante


def determinar_estado(promedio_estudiante):
    if promedio_estudiante >= 3.0:
        return "Aprueba"
    else:
        return "Reprueba"


# Manuel moreno