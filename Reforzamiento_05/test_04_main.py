"""
Módulos

4. Creando un archivo principal donde llamará a un módulo (operaciones.py)
el cuál contendrá las siguientes funciones:

-La primera función cargará a 3 números enteros que pedirá al usuario
que ingrese por consola un valor.
-La segunda función solamente sumará dos valores.
-Desde el archivo principal importar al módulo y sumar dos valores
usando las funciones anteriormente creadas en el módulo.
"""
from operaciones_test4 import entero, suma

def main():
    entero1, entero2, entero3 = entero()
    suma(entero1, entero2, entero3)

if __name__ == "__main__":
    main()

