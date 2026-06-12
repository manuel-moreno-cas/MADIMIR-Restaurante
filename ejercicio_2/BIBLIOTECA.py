def calcular_costo(categoria,dias):
    if categoria == "novela":
        costo_dia = 500
    elif categoria == "ciencia":
        costo_dia = 800
    elif categoria == "historia":
        costo_dia = 600
    else:
        costo_dia = 0
    total = costo_dia * dias
    return total

def categorias_mas_solicitadas(lista_categorias):
    conteo_novelas = 0
    conteo_ciencias = 0
    conteo_historias = 0
    for categoria in lista_categorias:
        if categoria == "novela":
            conteo_novelas += 1
        elif categoria == "ciencia":
            conteo_ciencias += 1
        elif categoria == "historia":
            conteo_historias += 1

print("ingrese su nombre")
nombre = input()
print("ingrese su edad")
edad = input()
print("ingrese la categoria de su libro")
categoria = input()
print("ingrese la dias")
dias = input()

for categoria in categorias_mas_solicitadas:
    if categoria == "novela":
        total = calcular_costo(categoria,dias)
    elif categoria == "ciencia":
        total = calcular_costo(categoria,dias)
    elif categoria == "historia":
        total = calcular_costo(categoria,dias)


print("*** REPORTE DEL DIA ***")
print("total de prestamos registrados", total)
print("categorias mas solicitadas", categorias_mas_solicitadas)



