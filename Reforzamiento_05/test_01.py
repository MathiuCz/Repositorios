"""
Exepciones

1. Crear una función la cual tendrá una excepción para que tu programa
no se bloquee donde se imprime un mensaje al usuario
la causa y/o solución (Pedir nombre por consola), solo aceptará string como input:
Si ingresa un entero, crear una excepción
La salida de función tendrá que tener el siguiente mensaje:

 "¡Hola NOMBRE!, hoy estamos DÍA de MES del AÑO"

 Ejemplo:
# ¡Hola Leonardo!, hoy estamos 04 de Mayo del 204

La función también deberá captar la fecha actual, de allí pasará a
tomar solo los datos que necesita para el examen final

"""
from datetime import datetime

def funtion():
    while True:
        try:
            nombre = input("Ingresa tu nombre: ")
            if nombre.isdigit():
                raise TypeError("El nombre no puede ser un número. Por favor, ingresa un nombre válido.")

            # Obtener fecha actual
            hoy = datetime.now()
            dia = hoy.strftime("%d")
            mes = hoy.strftime("%B")
            anio = hoy.strftime("%Y")

            print("¡Hola {}, hoy estamos {} de {} del {} .".format(nombre, dia, mes, anio))
            break

        except TypeError as te:
            print(te)

funtion()
