#Desarrollar un programa en Python que permita registrar información básica
# de estudiantes y determinar su estado académico utilizando una estructur
# organizada por capas.

def cal_promedio(nota1,nota2,nota3):
    promedio = (nota1 + nota2 + nota3) / 3
    return promedio
def deter_estado(promedio):
    if promedio >= 3.0:
        return "USTED APROBO"
    else:
        return "USTED REPRUEBA"

    # MANUEL MORENO