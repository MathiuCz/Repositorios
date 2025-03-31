"""3. Convertir tu diccionario a una lista y mostrar en consola el tipo de datos
final que tiene."""

#Creando diccionario
d1 = {
    "nombre" : "Mathius",
    "edad" : 20,
    "salario" : 20000
}
print("El diccionario original es {}.".format(d1))

#Convirtiendo el diccionario en una lista
lista_1 = list (d1.values()) #Solo los valores estoy considerando en la lista
print("Convirtiendo el diccionario a lista: {}.".format(lista_1))

#Agregando dni
d1["dni"] = 72745866

#mostrando los valores de salario y dni
print("El D.N.I es {} y su salario es {}.".format(d1["dni"], d1["salario"]))

#Eliminando el key edad
del d1["edad"]

#Mostrando el diccionario actualizado
print("El diccionario actualizado es {}.".format(d1))

#convirtiendo el diccionario en lista
lista_2 = list (d1.values()) #Solo los valores estoy considerando en la lista
print("La lista actualizada es {}.".format(lista_2))

#Mostrando el tipo de datos de la lista
print("El tipo de dato del primer item de la lista es {}.".format(type(lista_2[0])))
print("El tipo de dato del segundo item de la lista es {}.".format(type(lista_2[1])))
print("El tipo de dato del tercer item de la lista es {}.".format(type(lista_2[2])))