"""Crea una lista vacía, luego ingresa sus valores (10 valores numéricos) y
finalmente muestra la suma y la media de los números ingresado insertados en
la terminal
"""
#Lista vacia
numeros = []

#Agregando 10 valores numericos,
numeros.append(1)
numeros.append(2)
numeros.append(3)
numeros.append(4)
numeros.append(5)
numeros.append(6)
numeros.append(7)
numeros.append(8)
numeros.append(9)
numeros.append(10)
#Tambien se puede hacer con numeros.extend([1,2,3,4,5,6,7,8,9,10])
print("Mi lista es: {}".format(numeros))

#Suma de los numeros ingresados
suma_numeros = sum(numeros)

 #media arimetica de los numeros ingresados
media_numeros = sum(numeros) / len(numeros)

print("La suma de los datos es: {}".format(suma_numeros))
print("La media de los datos es: {}".format(media_numeros))


