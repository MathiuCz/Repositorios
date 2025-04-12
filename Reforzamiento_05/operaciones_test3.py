import random

def num_aleatorio():
    lista = [random.randint(0, 100) for _ in range(30)]
    print("La lista es: ")
    print(lista)
    return lista

def ordenar(lista):
    lista_ordenada = sorted(lista)
    print("La lista ordenada es: ")
    return lista_ordenada

def maximo(lista):
    maximo = max(lista)
    print("La lista maximo es: ", maximo)
    return maximo

