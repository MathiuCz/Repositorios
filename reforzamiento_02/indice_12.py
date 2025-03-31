
"""12. Crear una lista donde los primeros 2 datos serán, tu nombre y apellido paterno,
habrán también diferentes tipos de datos (enteros, flotantes, string y booleans - 9
datos, puede haber tipos de datos repetidos), crear otra lista con números pares (6
números) y sumarlo a la anterior lista en una variable para luego mostrar las 3 listas en
pantalla (observar y comentar que sucede al sumar listas)"""

#Lista mixta
list1 = ["Mathius", "Conde", 10, 20 , 4.5, 9.4, "galleta", "fisica", True]
#Lista de numeros pares
pares = [2, 4, 6, 8, 10, 12]
#suma de listas
sum_listas = list1 + pares

print("la lista 1 es: {}".format(list1))
print("La lista de numeros pares es : {}".format(pares))
print("La suma de las listas es: {}".format(sum_listas))

"""
Comentario

Observamos que tenemos dos listas como se nos asignó, representadas con las variables list1 y pares, 
ahora cuando sumamos las dos listas los elementos de la lista 'pares' se concatenan sin alterar el orden de los elementos
de la lista 'list1' y le asignamos la variable 'sum_listas' representando que es la suma de las dos listas anteriores.
"""
