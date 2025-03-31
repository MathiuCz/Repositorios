"""9. Crear un programa en Python donde tendrás una lista con 5
departamentos, ingresarás 2 departamentos adicionales por posición, el
cual el segundo departamento estará en la posición ‘1’ y el primero en
penúltimo lugar, finalmente mostrar la lista original y la lista actualizada
en terminal"""

departamentos = ["Lima", "Arequia", "Junin", "Loreto", "Trujillo"]

print("La lsita de departamentos es: {}".format(departamentos))
print("_______________________________________________________________________________")

#Primer departamento adicionado
dep_1 = "Ica"
#Segundo departamento adicionado
dep_2 = "Cajamarca"

#Primer departamento en la penultima posicion
departamentos.insert(4, dep_1)
#Segundo departamento en la posicion "1"
departamentos.insert(1, dep_2)

print("La lista actualizada de departamentos es: {}".format(departamentos))