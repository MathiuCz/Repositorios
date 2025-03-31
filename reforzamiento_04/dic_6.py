"""6. Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario."""

#Ingresando la cantidad de numeros en este caso 4
while True:
    try:
        tam= int(input("Ingresa la cantidad de numeros: "))
        if tam > 0:
            break
        else:
            print("Ingrese un número positivo")
    except ValueError:
        print("Entrada no valida. Ingrese un numero positivo")

#Creando el diccionario
dic = {}

#Aginando claves y valores
for i in range(tam):
    clave = int(input("Ingrese los numeros: "))
    valor = clave**3
    dic[clave] = valor

print("El diccionario con los valores es: {}. ".format(dic))



