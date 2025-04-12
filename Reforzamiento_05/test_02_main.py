"""
Módulos

2. Creando un archivo principal (main.py) donde importará a un módulo
(operaciones_test2.py) el cuál contendrá las siguientes funciones:
- Una función que realizará la carga de un valor entero y que verifique
que solamente tiene que ser numérico
- Una función que mostrará por pantalla la raíz cuadrada de dicho valor
- Y otra función el valor elevado al cuadrado y al cubo de dicho número,
puedes devolver un diccionario
- Utilizar el módulo math de python

"""

from operaciones_test2 import entero, raiz_cuadrada, potencia

def main():
    numero = entero()
    raiz = raiz_cuadrada(numero)
    potencias_resultado = potencia(numero)

    print("la raiz cuadrada es: ", raiz)
    print("{} al cuadrado es: {}".format(numero, potencias_resultado["cuadrado"]))
    print("{} al cubo es: {}".format(numero, potencias_resultado["cubo"]))
if __name__ == "__main__":
    main()