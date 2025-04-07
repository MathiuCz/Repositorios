"""
Programación funcional con Python (POO)

Requisitos:
    - Crear una función que multiplicará 3 valores y luego restará el segundo parámetro
    - Para esta función el tercer parámetro contendrá un valor
    - Mostrar 2 casos donde se ingrese los valores donde uno no afectará
    el valor del parámetro que ya contiene un valor
    y otro donde si lo estará afectando
"""
num_1 = int(input("Ingresa un numero: "))
num_2 = int(input("Ingresa otro numero: "))
num_3 = int(input("Ingresa otro numero: "))

#Definimos la funcion
def resta(a, b, c = 5):
    mul = a * b * c
    var_1 = mul - b
    return var_1
#No afecta el valor que tiene la variable c
print(resta(num_1, num_2))

#Si afecta el valor que tiene la variable c
print(resta(num_1, num_2, num_3))

