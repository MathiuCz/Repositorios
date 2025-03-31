"""8. Crear una agenda basada en un diccionario donde los key serán los nombres
de las personas y sus “values” serán los números de teléfono de c/u.
Ingresarás por consola el nombre y el número de cada persona que serán
registrados en la agenda.
El programa también te permitirá buscar por nombre en el diccionario en caso
no exista mostrar un mensaje de “No se encuentra registrado en la agenda”"""

#Cuantas personas quiere agendar
while True:
    try:
        tamano_agenda = int(input("Ingrese cuantas personas quiere guardar en su agenda: "))
        if tamano_agenda > 0 :
            break
        else:
            print("Ingrese un numero valido.")
    except ValueError:
        print("Entrada no valida. Ingrese un numero valido.")

#Creado mi diccionario
agenda = {}

#Agendando
for i in range(tamano_agenda):
    nombres = input("Ingrese nombres de la persona que quiere agendar: ")
    tel = input("Ingrese el numero de telefono de la persona que quiere agendar: ")
    agenda[nombres] = tel
print("Los nombres agendados con sus respectivos numeros son: {}.".format(agenda))
print("________________________________________________________________________________")

#Buscando si existe en la lista
while True:
    find = input("Ingrese el nombre de la persona que quiere buscar: ")
    if find in agenda:
        print("El numero de {} es {}".format(find, agenda[find]))
        break
    else:
        print("No se encuentra registrado en la agenda. Intente con un nombre que si este")