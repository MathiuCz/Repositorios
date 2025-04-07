"""
Ejercicio de intervención

Requisitos:
- Agregar una exepción donde se va a considerar una lista con 4 valores,
todos sus datos serán string
- Al querer modificar una de las posiciones no existentes
crear un nuevo índice y darle el valor de "0"
- Mostrar la lista final
"""

mi_lista = ["uno", "dos", "tres", "cuatro"]
print("Lista original: {}".format(mi_lista))

indice = int(input("Ingrese el índice que desea modificar: "))
nuevo_valor = input("Ingrese el nuevo valor para ese índice: ")

try:
    mi_lista[indice] = nuevo_valor
except IndexError:
    print("Índice fuera de rango. Se agregará un nuevo elemento con valor '0'.")
    mi_lista.append("0")

print("Lista final: {}".format(mi_lista))