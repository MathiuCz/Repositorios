"""Usando las propiedades de cadenas o string"""

"""
Requisitos:
 - Ingresar tu nombre y apellido por consola 
 (cada valor tiene que estar en una variable distinta)
 - Obtener el tamaño de tu nombre y apeellido completo luego de concatenarlos
 y mostrar en consola
 - Imprimir el resultado de la concatenación final todo en mayúsculas
 - Indicar mediante condicionales si el tamaño del nombre es mayor 
 o no al del apellido ingresado
 (Ingresar solo en este caso el apellido paterno)
 """
nombre = input("Ingresar tu nombre: ")
apellido = input("Ingresar tu apellido: ")

#Concatenacion
nombre_completo = nombre + " " + apellido
print("Mi nombre completo es ",nombre_completo)
print("El tamaño de mi nombre completo es ",len(nombre_completo)) #Incluye el espacio en la concatenacion

#Poniendo en mayusculas
print("Mi nombre completo en mayusculas es {}".format(nombre_completo.upper()))

#Condicional
if len(nombre) > len(apellido):
    print("EL tamaño del nombre es mayor que el apellido")
else:
    print("EL tamaño del apellido es mayor que el nombre")