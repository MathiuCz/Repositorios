
"""11. Identificar qué tipo de dato se obtiene al elevar tu edad con exponente 5 y luego
dividirlo por 10. Mostrar el resultado de su módulo con 3 en pantalla
"""
#Mi edad
edad = 20
#Exponente 5
exp = 5
#Edad elevada a la 5 y luego dividida por 10
resultado = pow(edad, exp) /10
#Modulo 3
mod = resultado % 3


print("El tipo de dato de mi edad elevada a la 5 dividida por 10 es: {}".format(type(resultado)))
print("El modulo con 3 es: {}".format(mod))
print("El tipo de dato del modulo con 3 es: {}".format(type(mod)))
