"""2. Crear un programa en Python donde tendrás una lista con 5 departamentos,
el programa te pedirá ingresar 2 departamentos el cual el segundo
departamento que ingreses sustituirá al primero de la lista."""

#Lista con 5 departamentos
dep = ["Lima", "Arequipa", "Juliaca", "Iquitos", "Trujullo"]

#Ingresando dos departamentos
dep_1 = input("Ingrese un departamento: ")
dep_2 = input("Ingrese un departamento: ")

#Ingresando el segundo departamento en el indice 0
dep.insert(0, dep_2)
dep.append(dep_1)

print("La lista actualizada es: {}.".format(dep))
