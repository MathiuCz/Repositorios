"""
    Programación Orientada a Objetos
    Participación

Requerimientos:
    - Crear una Clase Alumno
    - Debe tener un atributo de nacionalidad con el valor "Peruano"
    - Tendrá 3 notas, la nota inicial de c/u será de 0
    - Crear un método que indicará el promedio del alumno
    - Crear un método que indicará si el alumno está aprobado o no de acuerdo a su promedio
    - Las notas serán pasadas por parámetro al momento de instanciar la clase
    - Crear un método para obtener el nombre y distrito de residencia del alumno
    - Instanciar la clase para el caso de 2 alumnos necesariamente
"""
class Alumno:
    #Atributo
    nacionalidad = "Peruano"

    def __init__(self, nombre, distrito, nota1=0, nota2=0, nota3=0):
        self.nombre = nombre
        self.distrito = distrito
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    #Calculando el promedio
    def promedio(self):
        prom = (self.nota1 + self.nota2 + self.nota3) / 3
        return prom

    #Veremos si aprobó o no
    def aprobado(self):
        if self.promedio() > 10.5:
            return "Aprobado"
        else:
            return "No aprobado"

    def info(self):
        return "Nombre: {}, distrito: {}".format(self.nombre, self.distrito)

#Dos alumnos
alumno_1 = Alumno("Mathius Conde", "la Victoria", 14, 5, 20)
alumno_2 = Alumno("Maria Rodriguez", "San Borja", 14, 9, 15)

for alumno in (alumno_1, alumno_2):
    print("______________________________________")
    print(alumno.info())
    print(f"Nacionalidad: {alumno.nacionalidad}")
    print(f"Promedio: {alumno.promedio():.2f}")
    print(f"Estado: {alumno.aprobado()}")