
"""13. Crear una lista de 6 objetos (datos) y mostrarlos en pantalla (ítems de cursos que
lleves o hayas llevado en la universidad)
Luego agregar 4 Objetos nuevos a tu lista y mostrarla también en pantalla."""

#lista de 6 datos
cursos = ["Mecanica Cuantica", "Electromagnetismo", "Termodinamica", "Fisica Electronica", "Mecanica Clasica", "Fisica Computacional"]

print("Lista de cursos inicial: {}".format(cursos))

#Agregando nuevos elementos a la listas

cursos.extend(["Calculo Avanzado", "Redaccion y metodologia cientifica", "Fisica Estadistica", "Estado solido"])
print("Lista de cursos actualizada: {}".format(cursos))