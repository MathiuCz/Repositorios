"""1. Escribir un programa donde ingresarás el tamaño de la lista mediante
consola, este tamaño servirá para ingresar una cantidad X de nombres de
alumnos. Ingresarás los nombres mediante consola también.
Se quiere mostrar finalmente el tamaño de la lista y todos los nombres de
la lista que fueron ingresados."""

#Ingresando la cantidad de datos
while True:
    try:
        tam_list = int(input("Ingresa la cantidad de nombres en la lista: "))
        if tam_list > 0:
            break
        else:
            print("Ingrese un número positivo")
    except ValueError:
        print("Entrada no valida. Ingrese un numero positivo")

#Lista vacia
lista_nombres = []

#Ingresando los nombres de acuerdo a la cantidad de datos ingresados
for i in range(tam_list):
    nombre = input("Ingresa el nombre del alumno: ")
    lista_nombres.append(nombre)

#Mostrando en pantalla
print("La lista actualizada es: {}".format(lista_nombres))
print("La lista contiene {} nombres.".format(len(lista_nombres)))


