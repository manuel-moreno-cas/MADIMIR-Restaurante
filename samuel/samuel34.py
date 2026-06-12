# crea dos conjuntos con nombres de estudiantes de dos cursos diferentes
# y muestra la union de ambos conjuntos

curso_a = {"juan","ana","maria","pedro","luis"}
curso_b = {"carlos", "ana", "sofia", "luis", "camila"}

union_estudiantes = curso_a.union(curso_b)

print("estudiantes del curso a:", curso_a)
print("estudiantes del curso b:", curso_b)
print("\n union de ambos cursos:")
print(union_estudiantes)
