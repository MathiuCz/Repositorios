"""5. Ingresar el nombre de tu carrera dentro de los valores que tienes en tu
diccionario.
- Mostrar en consola los valores de tu carrera y nombre agregándolos a
una variable c/u"""

#diccionario
d1 = {
    "nombre" : "Mathius",
    "edad" : 20,
    "salario" : 20000
}
d1["carrera"] = "Física"

#Asignando varibles
var1 = d1["nombre"]
var2 = d1["carrera"]

#Imprimiendo los valores de carrera y nombre

print("Hola soy {} y estudio {}.".format(var1, var2))