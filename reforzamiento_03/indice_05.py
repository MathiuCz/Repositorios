"""5. Crear una lista (entre floats y bools, 6 elementos mínimo) donde imprimas el
penúltimo y antepenúltimo valor (por índice). Reconocer cada uno de los tipos
de datos en esta lista creada y mostrar los resultados en consola"""

#Lista con floats y booleans
list = [True, False, 4.3, 7.5, 9.5, True, 12.4, False]

print("La lista es: {}.".format(list))
print("_______________________________________________________")

#Imprimiento el antepenultimo y penultimo valor de la lista
print("El penultimo valor es: {}".format(list[6]))
print("El antepenultimo valor es: {}".format(list[5]))
print("_____________________________________________________________")

#Reconociendo los tipos de datos en esta lista
print("Tipos de datos")
print("El dato numero 1 es {} y es un dato de tipo: {}".format(list[0], type(list[0])))
print("El dato numero 2 es {} y es un dato de tipo: {}".format(list[1], type(list[1])))
print("El dato numero 3 es {} y es un dato de tipo: {}".format(list[2], type(list[2])))
print("El dato numero 4 es {} y es un dato de tipo: {}".format(list[3], type(list[3])))
print("El dato numero 5 es {} y es un dato de tipo: {}".format(list[4], type(list[4])))
print("El dato numero 6 es {} y es un dato de tipo: {}".format(list[5], type(list[5])))
print("El dato numero 7 es {} y es un dato de tipo: {}".format(list[6], type(list[6])))
print("El dato numero 8 es {} y es un dato de tipo: {}".format(list[7], type(list[7])))