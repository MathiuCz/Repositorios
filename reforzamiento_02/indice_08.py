
"""8.Usando la condicional if imprimir por pantalla si una lista está vacía o no, probar con
una lista vacía y otra con una lista no vacía."""

#Lista vacia
lista1 = []
#tamaño de la lista
tam1 = len(lista1)

if tam1 == 0:
    print("La lista esta vacia")
else:
    print("La lista tiene {} valores".format(tam1))

# Probando para una lista no vacia

print("___________________________")

#lista con elementos
lista2 = ["chedar", 27, 3.4, True]
#tamaño de la lista
tam2 = len(lista2)

if tam2 == 0:
    print("La lista esta vacia")
else:
    print("La lista tiene {} elementos".format(tam2))




