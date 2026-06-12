#Solicite tres números e indique cuál es el mayor.

num1 = float(input("ingrese el primer numero"))
num2 = float(input("ingrese el segundo numero"))
num3 = float(input("ingrese el tercer numero"))

if num1 > num2 and num1 > num3:
    print("el primer numero es el mayor")
elif num1 < num2 and num2 > num3:
    print("el segundo numero es el mayor")
elif num2 < num3 and num1 < num3:
    print("el tercer numero es el mayor")
else:
    print("los tres numeros son igusles")

print("\n*** FIN DEL PROGRAMA ***")
print("\n*** GRACIAS ***")

#MANUEL MORENO