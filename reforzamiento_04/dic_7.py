"""7. Realizar un programa donde se ingresarán por consola los nombres de los
alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso
y las notas de c/u. Guardarás la información en un diccionario donde las claves
serán los nombres de c/u de estos alumnos y sus valores serán las notas de
esto alumnos. Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas.
"""

#Ingresando la cantidad de dalumnos
while True:
    try:
        tam_list = int(input("Ingresa la cantidad de alumnos: "))
        if tam_list > 0:
            break
        else:
            print("Ingrese un número positivo")
    except ValueError:
        print("Entrada no valida. Ingrese un numero positivo")

#Creando diccionario
dic = {}

#Asignando claves y valores
for i in range(tam_list):
    clave = input("Ingresa los nombres de los alumnos: ")
    while True:
        try:
            notas = float(input("Ingresa las notas de los alumnos: "))
            if 0 <= notas <= 20:  # Suponiendo una escala de 0 a 20
                break
            else:
                print("La nota debe estar entre 0 y 20.")
        except ValueError:
            print("Entrada no valida. Ingrese un numero valido")
    dic[clave] = notas

#Escribiendo el mensaje
for clave, notas in dic.items():
    print("{} tiene la nota de {}.".format(clave, notas ))

#media
media = sum(dic.values())/tam_list
print("La media arimetica de las notas es {}.".format(media))
