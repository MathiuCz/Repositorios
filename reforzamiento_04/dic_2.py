"""2. Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado."""

#Creando diccionario
d1 = {
    "nombre" : "Mathius",
    "edad" : 20,
    "salario" : 20000
}
print("El diccionario original es {}.".format(d1))
#Convirtiendo el diccionario en una lista
lista_1 = list (d1)
print("Convirtiendo el diccionario a lista: {}.".format(lista_1))

#Agregando dni
d1["dni"] = 72745866

#mostrando los valores de salario y dni
print("El D.N.I es {} y su salario es {}.".format(d1["dni"], d1["salario"]))

#Eliminando el key edad
del d1["edad"]

#Mostrando el diccionario actualizado
print("El diccionario actualizado es {}.".format(d1))
