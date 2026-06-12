
# SISTEMA DE GESTIÓN ACADÉMICA

estudiantes = {}
cantidad = int(input("¿Cuántos estudiantes desea registrar?: "))
for i in range(cantidad):
    print("\nESTUDIANTE", i + 1)

    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    documento = input("Documento: ")

    informacion = (nombre, edad, documento)

    cursos = set()

    num_cursos = int(input("¿Cuántos cursos tiene?: "))

    notas = {}

    for j in range(num_cursos):
        curso = input("Nombre del curso: ")
        cursos.add(curso)

        nota = float(input("Nota de " + curso + ": "))
        notas[curso] = nota

    promedio = sum(notas.values()) / len(notas)

    estudiantes[nombre] = {
        "informacion": informacion,
        "cursos": cursos,
        "notas": notas,
        "promedio": promedio
    }

buscar = input("\nIngrese el nombre del estudiante a buscar: ")

if buscar in estudiantes:
    print("\nESTUDIANTE ENCONTRADO")
    print("Información:", estudiantes[buscar]["informacion"])
    print("Cursos:", estudiantes[buscar]["cursos"])
    print("Notas:", estudiantes[buscar]["notas"])
    print("Promedio:", round(estudiantes[buscar]["promedio"], 2))
else:
    print("Estudiante no encontrado.")

mejor_estudiante = max(
    estudiantes,
    key=lambda x: estudiantes[x]["promedio"]
)

print("\n===== MEJOR ESTUDIANTE =====")
print("Nombre:", mejor_estudiante)
print("Promedio:", round(estudiantes[mejor_estudiante]["promedio"], 2))

print("\n===== REPORTE FINAL =====")

for nombre, datos in estudiantes.items():
    print("\nNombre:", nombre)
    print("Información:", datos["informacion"])
    print("Cursos:", datos["cursos"])
    print("Notas:", datos["notas"])
    print("Promedio:", round(datos["promedio"], 2))

#manuel moreno