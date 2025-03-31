
"""5.Crear un programa que parte creando un sueldo en una variable, sepamos si es par
o impar mediante un mensaje. Utilizar módulo y condicional (if)."""

#Creamos un sueldo
sueldo = 3562     #Se puede poner otro valor

#Usando el operador modulo
modulo = sueldo % 2

#Condicional
if modulo == 0:
    print("El sueldo es par.")
else:
    print("El sueldo es impar.")