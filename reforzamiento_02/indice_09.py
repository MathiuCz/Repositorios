
"""9.Elevar una base al exponente de 6 (que estará dentro una variable), este número el
cual su valor estará asignado a una variable y luego restar este mismo valor multiplicado
por dos (usar pow o **). Mostrar el resultado final en pantalla."""

#Elegimos una base
base = 4
#Exponente 6
exp = 6
#Resultado de la potencia
potencia = pow(base, exp)

#Restando la potencia menos dos veces su valor
rest = potencia - (2 * potencia)

print("El resultado es: {}".format(rest))

