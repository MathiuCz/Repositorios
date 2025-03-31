"""3. Tienes una lista con 5 nombres de estudiantes. Crear un programa que te
pedirá ingresar el nombre de un estudiante, la cuál será eliminada de lista
inicial en caso que no exista en la lista mostrar un mensaje donde indique
que no se encuentre en la lista y esta será agregada a la lista.
 Finalmente mostrar la lista actualizada en consola."""

#Lista con 5 nombres
nombres = ["Rodrigo", "Lucas", "Amir", "José", "Ricardo"]

estudiante = input("Ingrese el nombre del estudiante: ")

#Se elimina o se agrega el nombre
if estudiante in nombres:
    print("El nombre del estudiante se encuenta de la lista.")
    nombres.remove(estudiante)
    print("La lista actualizada es: {}.".format(nombres))
else:
    print("El nombre del estudiante no se encuentra en la lista.")
    nombres.append(estudiante)
    print("La lista actualizada es: {}.".format(nombres))