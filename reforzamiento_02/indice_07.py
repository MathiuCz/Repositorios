
"""7.De 3 números asignados (entre positivos y negativos tú los propones) a 3 variables, se
pide hallar la suma de los valores de los módulos con 3, 5, y 7 respectivamente, mostrar
en pantalla el valor de la suma."""

#Numeros (positivos y negativos) asignados a cada variable
n_1 = -10
n_2 = 30
n_3 = -58

#Modulo con 3, 5 y 7 respectivamente
m_1 = n_1 % 3
m_2 = n_2 % 5
m_3 = n_3 % 7

#Suma de los modulos
sum = m_1 + m_2 + m_3

print(m_1, m_2, m_3) #El operador modulo me devuelve los residuos positivos
print("La suma de los modulos es {}".format(sum))