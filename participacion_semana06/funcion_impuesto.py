"""
Ejercicio de intervención

Requisitos:
1. Crear un módulo donde se va a tener que crear una función que obtiene
el impuesto que va a pagar una persona si el sueldo es mayor a 500 soles,
impuesto: 8%

2. Esta función usará una exception si el sueldo es tipo string

3. Pedir el sueldo por consola en el archivo principal

4. El archivo principal importará a la función creada para ser usada

"""

def impuesto(sa):
    try:
        if sa > 500:
            imp = (sa * 0.08)
            print("Su impuesto es de S/.{}".format(imp))
    except TypeError:
        print("No se puede usar un string como un dato")

