
"""2.Crea una variable tipo int. Luego, multiplica por 10 y restarle el valor de 10. Debes
hacer todo esto en dos pasos. Finalmente convertirlo a float y mostrar el resultado
por pantalla y el tipo de variable."""

# Creacion de la variable int
valor_int = 30
# Las operaciones en 2 pasos
mult = 10 * valor_int
resta = mult - 10

# Convirtiendo la resta a flotante
flo_rest = float(resta)

print("El resultado es: {}.".format(flo_rest))
print("El tipo de variable es {}.". format(type(flo_rest)))
