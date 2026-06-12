#Solicite una nota (0 a 5) e indique si el estudiante aprueba (>=3.0) o no.

nota = float(input("ingrese su nota: "))

if nota >5 or nota <0:
     print("nota no valina")
elif nota >= 3.0:
     print("el estudiante aprobo")
else:
     print("el estdiante reprobo")

print("\n*** FIN DE LA OPERACION ***")
print("\n*** GRACIAS***")

#MANUEL MORENO
