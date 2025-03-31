"""Elimina ahora todos los elementos de la lista creada previamente y mostrar en
consola la lista actualizada agregando tu nombre, apellido paterno, apellido
materno y edad"""

#Lista creada previamente
list = [True, False, 4.3, 7.5, 9.5, True, 12.4, False]

#Eliminando los elementos de la lista previa
list.clear()
print(list)
print("La lista tiene {} elementos".format(len(list)))
print("___________________________________________________")

#Agregando nuevos datos a la lista
list.extend(["Mathius", "Conde", "Zavaleta",20])
print("la lista actualizada es: {}".format(list))
