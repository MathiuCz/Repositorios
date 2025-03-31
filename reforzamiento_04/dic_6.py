"""6. Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario."""

#Creando el diccionario
dic = {}

#Aginando claves y valores
for i in range(4):
    clave = int(input("Ingrese los numeros: "))
    valor = clave**3
    dic[clave] = valor

print("El diccionario con los valores es: {}. ".format(dic))



