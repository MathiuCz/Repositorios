"""Diccionarios:
1. Crea correctamente un diccionario con los campos de: nombre, edad, salario
y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la
terminal.
"""

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

