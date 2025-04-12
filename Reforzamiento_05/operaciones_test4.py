
def entero():
    while True:
        try:
            valor1 = int(input("Ingrese un numero: "))
            valor2 = int(input("Ingrese otro numero: "))
            valor3 = int(input("Ingrese otro numero: "))
            return valor1, valor2, valor3
        except ValueError:
            print("El valor ingresado no es un entero")


def suma (valor1, valor2, valor3):
    print("La suma es: ", valor1 + valor2)
    return valor1 + valor2
