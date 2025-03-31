
""" 1. Agregar 5 Objetos nuevos a tu lista (append) y quitar 2 elementos de esta
lista por valor. Mostrar la lista final en la terminal.
Obtén también la cantidad total ítems que tienes en tu lista ya creada para
agregar este valor a tu lista y mostrar también el resultado final de cantidad
total de elemento y la lista actualizada en consola. """

consolas = ["PS1", "PS2", "Nintendo Switch"] #3 datos iniciales

#Agregando 5 objetos a mi lista
consolas.append("Xbox one")
consolas.append("Nintendo Switch Oled")
consolas.append("Atari")
consolas.append("PSP")
consolas.append("Nintendo Ds")

print("Mi lista es : {}".format(consolas))
print("Mi lista tiene {} datos.".format(len(consolas)))
print("_______________________________________________________")

#Quitando valores de la lista por valor
consolas.remove("Atari")
consolas.remove("PSP")

print("Mi lista actualizada es : {}".format(consolas))

#Cantidad total
print("Mi lista actualizada tiene {} datos.".format(len(consolas)))
print("_______________________________________________________")

#Agregando la cantidad de datos que tiene mi lista a la lista
cant_total = len(consolas)
consolas.append(cant_total)

print("Mi lista actualizada con la cantidad de valores es : {}".format(consolas))
print("Mi lista tiene {} datos.".format(len(consolas)))