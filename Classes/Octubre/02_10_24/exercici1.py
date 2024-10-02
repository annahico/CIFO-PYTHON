# A) llista strings

import re

["2, 3, hola, 24, 34.000, hola2 \n", "3,4, hola, 24, 54.000, hola3, \n",
    "3,4, hola, 24, 54.000, hola3\n", "3,4, hola3"]

cadena = "2, 3, hola, 24, 34.000, hola2 \n"

patro = re.compile("[a-z0-9\\.]+")
patro.findall(cadena)
# --> elimimar els . de milers ✔️
# --> espais davant i darrere
# --> eliminar \n final de cada string ✔️
# --> split per la coma ","

llista = ["2, 3, hola, 24, 34.000, hola2 \n", "3,4, hola, 24, 54.000, hola3, \n",
          "3,4, hola, 24, 54.000, hola3\n", "3,4, hola3"]

# llista = [item.replace(".", "") for item in llista]
# print(llista)

# llista = [item.replace("\n", "") for item in llista]
# print(llista)


# B) fila de files o matrius ✔️

# Matriu inicial
matriu = [[2, 3, "hola", 24, 34000, "hola2"], []]

# Accés a elements individuals
print(matriu[0][0])
print(matriu[0][2])

matriu[1].extend([5, 6, 7])  # Afegim elements a la segona fila
print(matriu)

# Recórrer la matriu
for fila in matriu:
    print(fila)
