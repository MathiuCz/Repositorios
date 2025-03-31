"""9. Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura
“00054” y su value será el coste de la factura. El programa tendrá la opción
de pedir nueva factura (por consola) que se agregará al diccionario. Cada vez
que el área de contabilidad pague una factura se pedirá el número de factura
que fue cancelada, si existe mostrar un mensaje donde indicará “La factura
ya está cancelada” caso contrario “El número de factura no existe”
Considerar que cada vez que se realice algún pago o ingreso de una nueva
factura se mostrará inmediatamente al diccionario actualizado."""

#Diccionario ya creado
fact = {"00054" : 200.0, "00055": 300.0}

#Selecciones un numero
print("MENU")
print("1. Agregar nueva factura")
print("2. Pagar factura")
print("3. Mostrar facturas pedientes")
print("4. Salir")

while True:
    indice = int(input("Seleccione una opcion: "))

    match indice:
        case 1:
                factura = input("Ingrese el numero de factura que quiere añadir: ")

                if factura in fact:
                    print("El factura {} ya existe".format(factura))
                    break
                else:
                    costo = float(input("Ingrese el costo de la factura: "))
                    fact[factura] = costo
                    print("La factura {} se ha ingreado con exito.".format(factura))
                    print("Facturas registradas")
                    for factura, costo in fact.items():
                        print("Factura {}: S/.{}".format(factura, costo))
                break
        case 2:
            factura_pagar = input("Ingrese el numero de factura que se pagó: ")

            if factura_pagar in fact:
                print("La factura ya está cancelada")
                del fact[factura_pagar]
                print("Facturas que faltan pagar")
                for factura, costo in fact.items():
                    print("Factura {}: S/.{}".format(factura, costo))
            else:
                print("El numero de factura no existe")
            break

        case 3:
            print("Las facturas pendientes")
            for factura, costo in fact.items():
                print("Factura {}: S/. {}".format(factura, costo))
            break

        case 4:
            print("Saliendo del sistema...")
            break

        case _:
            print("Opción no valida")
            break
