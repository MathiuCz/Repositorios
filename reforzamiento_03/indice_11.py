"""11. Ingresar compañías relacionadas con al mundo de TI, copia los elementos
de la lista en otra lista pero estarán orden inverso, y muestra sus
elementos por la terminal y la lista original también.
"""
tec = ["NVIDIA", "SANSUNG", "INTEL", "AMD", "APPLE", "HUAWEI", "IBM", "MICROSOFT"]

tec_copy = tec.copy()

tec_copy.reverse()

print("Lista de empresas de tecnologia: {}".format(tec))
print("Lista de empresas de tecnologia al reves: {}".format(tec_copy))