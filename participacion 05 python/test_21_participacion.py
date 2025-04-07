"""
Programación funcional con Python (POO)

Requisitos:
    - Solicitar al usuario 4 números por consola
    - Crear una función que devuelva cuál es el número mayor de los 4
      ingresados por el usuario
    - Finalmente asignar a una variable el valor de esta función
      para elevar al cubo este resultado y mostrarlo en la terminal
"""

def funcion(a,b,c,d):
    if a > b and a > c and a > d:
        return (a)
    elif b > a and b > c and b > d:
        return (b)
    elif c > a and c > b and c > d:
        return (c)
    else:
        return (d)

#Solicitando numeros al usuario
num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un numero: "))
num3 = int(input("Ingrese un numero: "))
num4 = int(input("Ingrese un numero: "))

mayor = funcion(num1, num2, num3, num4)
cubo  = mayor ** 3

print("El numero mayor es : {}".format(mayor))
print("El numero cubo es : {}".format(cubo))