"""10. Tienes una lista con 7 diferentes nombres de BD relacionales. De la cual 3
BDs estarán repetidas adrede (en posiciones no consecutivas), sacar la
base de datos repetidas uno por valor y le otro por índice.
Finalmente mostrar la lista actualizada en consola."""

#Lista de BD con 7 difernetes nombres de DB relaciones con 3 repetidas
bd_list = ["MySQL", "PostgreSQL", "Oracle", "MySQL", "SQL Server", "PostgreSQL", "Oracle"]
print("Mi lista de base de datos es: {}.".format(bd_list))

#Piden sacar las base de datos repetidas tanto por valor como por indice

#Sacanado las bases de datos repetida por valor
bd_list.remove("MySQL")
bd_list.remove("PostgreSQL")
bd_list.remove("Oracle")
print("Mi lista de base de datos luego de eliminar por valor es: {}.".format(bd_list))
print("_________________________________________________________")

#Sacando las bases de datos repetidas por indice
bd_list_1 = ["MySQL", "PostgreSQL", "Oracle", "MySQL", "SQL Server", "PostgreSQL", "Oracle"]
print("Mi lista de base de datos es: {}.".format(bd_list_1))

del bd_list_1[3]
del bd_list_1[4]
del bd_list_1[2]

print("La lista de base de datos luego de eliminar por indice es: {}.".format(bd_list_1))
