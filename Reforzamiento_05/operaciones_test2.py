import math


def entero():
    while True:
        try:
            valor = int(input("Ingrese un numero: "))
            return valor
        except ValueError:
            print("El valor ingresado no es un entero")


def raiz_cuadrada(a):
    return math.sqrt(a)

def potencia(a):
    return {
        "cuadrado": math.pow(a,2),
        "cubo": math.pow(a,3),

    }