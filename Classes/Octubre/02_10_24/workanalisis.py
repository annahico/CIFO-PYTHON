import io
import re

patro = re.compile("[A-Za-z0-9 \\-_]+")

arxiu = io.open("arxiu del PC", "r", encoding='utf-8')

llistadecadenes = arxiu.readlines()
print(len(llistadecadenes))
matriz = []
for cadena in llistadecadenes:
    matriz.append(patro.findall(cadena))
print(matriz[0])
