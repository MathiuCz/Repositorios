"""4. Crea dos listas (una de datos string y la otra de datos numéricos) para luego
usar los métodos de orden (los elementos tienen que estar desordenados),
mostrar las listas antes y después de aplicarle los métodos de orden"""

#Lista de datos string
frutas = ["manzana", "pera", "platano", "mandarina", "lucuma", "albarecoque"]

#Lista de datos numericos
numbers = [20, 40, 10, 9, 35, 2, 5, 4, 50, 34]

print("La lista de frutas es: {}".format(frutas))
print("La lista de números es: {}".format(numbers))
print("_______________________________________________________")

#Ordenando las listas
frutas.sort()
numbers.sort()

#Listas ordenadas
print("La lista de frutas ordenada es es: {}".format(frutas))
print("La lista de numeros ordenada es: {}".format(numbers))