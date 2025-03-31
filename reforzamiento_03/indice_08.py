"""Escribir un programa donde ingresará 8 nombres de países. Se quiere
hacer un clon de la lista, esta copia se le eliminará el primer y penúltimo
valor, mostrar finalmente el tamaño de la lista modificada, la lista original
y todos sus elementos de la lista modificada."""

#Lista con 8 paises
paises = ["Perú", "Argentina", "Bolivia", "Ecuador", "USA", "Mexico", "Alemania", "España"]
print("La lista de paises es: {}".format(paises))
print("El tamaño de la lista es: {}".format(len(paises)))
print("_________________________________________________________________")

#Copiando la lista
paises_2 = paises.copy()

#Eliminando el primer y penultimo valor
print("El primer termino a eliminar es: {}".format(paises_2[0]))
print("El penultimo termino a elimianr es: {}".format(paises_2[6]))
print("_____________________________________________________________________")

#Quitando los datos
paises_2.pop(0) #Valor inicial, en listas se empieza a contar desde el 0
paises_2.pop(5) #Dado que se ha elimiando el primer elemento, el penultimo termino pasa a ser el 5

print("La lista actualziada es: {}".format(paises_2))
print("El tamaño de la lista actualziada es: {}".format(len(paises_2)))