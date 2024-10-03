import io
import re

patro = re.compile(r"[A-Za-z0-9\-': \\/.!$?]+|\"[^\"]*\"")


arxiu = io.open("C:\\Users\\Usuario\\Desktop\\Marvel_DC.csv",
                "r", encoding='utf-8')

llistadecadenes = arxiu.readlines()
print(len(llistadecadenes))
matriz = []
for cadena in llistadecadenes:
    matriz.append(patro.findall(cadena))
print(matriz[0])
