"""4. Ingresar por consola el tamaño de una lista, luego empezarás a ingresar los
datos mediante consola también (5 compañías relacionadas con al mundo de
TI) y harás una copia donde adrede agregarás nombres que estarán
repetidos (mediante consola) para que finalmente muestres otra lista donde
solo se mostrará los nombres no repetidos y también la lista inicial"""

#Ingresar un valor correcto para el tamaño de la lista
while True:
    try:
        tam_list = int(input("Ingresa el tamaño de la lista: "))
        if tam_list > 0:
            break
        else:
            print("Ingrese un número positivo")
    except ValueError:
        print("Entrada no valida. Ingrese un numero positivo")

empresas_1 = []

for i in range(tam_list):
    emp_1 = input("Ingrese en nombre de la empresa: ")
    empresas_1.append(emp_1)

empresas_2 = empresas_1.copy()

extra = int(input("¿Cuantas empresas desea repetir? "))

for i in range(extra):
    emp_2 = input("Ingrese en nombre de la empresa: ")
    empresas_2.append(emp_2)

empresas_3 = list(set(empresas_2))

print("La lista original es: {}".format(empresas_1))
print("La lista con empresas repetidas es: {}".format(empresas_2))
print("La lista sin empresas duplicadas es: {}".format(empresas_3))

