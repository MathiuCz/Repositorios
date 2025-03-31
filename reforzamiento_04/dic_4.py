"""4. Crear un diccionario con 6 departamentos en el país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.
- Comprobar que no existe este departamento borrado dentro del
diccionario."""

#diccionarios con departamentes
dep = {"dep1" : "Lima","dep2" : "La Libertad", "dep3" : "Tacna", "dep4" : "Trujillo", "dep5" : "Ica", "dep6" : "Ayacucho"}
del dep["dep1"] #borrando un departamento al azar
dep["dep5"] = "Iquitos" # actualizando dep 5 que es el penultimo

#Comprobando que no existe el departamento
existe = "Ica" in dep
print("¿Ica sigue en el diccionario?", existe)

print("El diccionario final es: {}.".format(dep))