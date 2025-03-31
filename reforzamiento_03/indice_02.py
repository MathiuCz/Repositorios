"""2. Devuelve la cantidad de veces que se repite un curso que hayas llevado en
pregrado (agregarlos previamente a la lista con un mínimo de 5 cursos) luego
mostrarla, finalmente elimina el segundo ítem de la lista usando debidamente
su índice y mostrar en consola tu lista actualizada"""
from itertools import count

curso_pregrado = ["Fisica Computacional", "Electromagnetismo", "Mecanica Cuantica", "Termodinamica", "Mecanica Clasica"]

#Agregando cursos para que se repitan
curso_pregrado.append("Fisica Computacional")
curso_pregrado.append("Fisica Computacional")
curso_pregrado.append("Fisica Computacional")
curso_pregrado.append("Electromagnetismo")
curso_pregrado.append("Electromagnetismo")
curso_pregrado.append("Mecanica Cuantica")

#Mostrando mi lista de cursos
print(curso_pregrado)
print("La cantidad de cursos que tiene la lista es de: {}".format(len(curso_pregrado)))
print("_____________________________________________________________________________")

#Mostrando los cursos que se repiten
print("La cantidad de veces que se repite Fisica computacional es: {}".format(curso_pregrado.count("Fisica Computacional")))
print("La cantidad de veces que se repite Mecanica Cuantica es: {}".format(curso_pregrado.count("Mecanica Cuantica")))
print("La cantidad de veces que se repite Electromagnetismo es : {}".format(curso_pregrado.count("Electromagnetismo")))
print("_____________________________________________________________________________")

#Eliminando el segundo item de la lista
del curso_pregrado[1] #el segundo item de la lista tiene el indice 1 en la lista ya que se cuenta desde el 0

print("Mi lista actualizada es: {}".format(curso_pregrado))
print("Mi lista tiene {} cursos".format(len(curso_pregrado)))