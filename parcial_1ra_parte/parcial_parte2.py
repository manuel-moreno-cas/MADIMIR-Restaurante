
# escribe un programa que calcule el salario de un empleado teniendo en cuenta lo siguiente:
#1. el salario basico es igual a 2 millones de peso
#2. se debe calcular salud y pension del 4% cada uno
#3. si el salario es inferior o  igual a lo que corresponde 1.5 salarios minimos tiene derecho al subcidio
# de transporte por 195 mil pesos
#4. se debe mostrar como resultado el valor del dia trabajado el salario basico
#las deducciones por salud y pension, el subcidio de transporte y el salario neto

salario = int(input("ingrese su salario:"))
salario_bas = int( 2000000)
salud = int( salario_bas * 0.04)
pensi = int( salario_bas * 0.04)

salario_min = 1750000

if salario <=(1.5 * salario_min):
    subsidio_trans = 195000

else:
    subsidio_trans = 0

valor_days =int( salario / 30)

salario_neto = salario - salud - pensi + subsidio_trans

print("\n---------- BIENVENIDO TRABAJADOR ----------\n")
print("su salario es:", salario,"pesos")
print("su valor del dia es:", valor_days, "pesos")
print("su descuento de salud:", salud, "pesos")
print("su descuento de pension:", pensi, "pesos")
print("subcidio de transporte:", subsidio_trans, "pesos")
print("salario neto:", int(salario_neto), "pesos")

print("\n---------- GRACIAS... ----------\n")

#MANUEL MORENO


