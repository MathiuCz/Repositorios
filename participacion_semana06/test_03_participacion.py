"""Control o gestión de excepciones"""

"""
Requisitos:
    - Crear una función aplicando exceptions donde el bloque except
    va a considerar a los errors de división entre cero y el tipo de error
    - Los valores tienen que ser mayor a 0
    - Los valores tienen que ser ingresado por consola
"""
#definimos la funcion
def division():
        try:
            numerador = float(input("Introduce un numerador: "))
            denominador = float(input("Introduce un denominador: "))

            if numerador< 0 or denominador< 0:
                raise ValueError("Ambos valores debe ser mayores a 0")

            result = numerador/ denominador
            print("El resultado de la division es: {}".format(result))

        except ZeroDivisionError:
            print("No se puede dividir entre cero")

        except ValueError:
            print("Error de valor")

division()
