"""3. Crea una siguiente lista vacía y agregue ítems a partir de variables (los cuales
tendrán los siguientes tipos de datos: 3 floats, 3 ints y 3 strings) (append).
Sumar las dos listas creadas anteriormente y mostrar el resultado en consola.
"""
#Lista creada con anterioridad en el ejercicio 2
curso_pregrado = ["Fisica Computacional", "Electromagnetismo", "Mecanica Cuantica", "Termodinamica", "Mecanica Clasica"]

#Creando listas vacias
lista_1 = []

#Creando variables
int_1, int_2, int_3 = 1, 2, 3
str_1, str_2, str_3 = 'Hola', 'python', 'PS5'
float_1, float_2, float_3 = 1.5, 2.5, 3.5

#Agregando datos a la lista 1
lista_1.append(int_1)
lista_1.append(int_2)
lista_1.append(int_3)
lista_1.append(float_1)
lista_1.append(float_2)
lista_1.append(float_3)
lista_1.append(str_1)
lista_1.append(str_2)
lista_1.append(str_3)

#sumando las dos listas
sum_listas = lista_1 + curso_pregrado

print("La suma de las listas es: {}".format(sum_listas))
print("La lista tiene {} datos.".format(len(sum_listas)))