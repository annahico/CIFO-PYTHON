import io
import re

patro = re.compile(r"[A-Za-z0-9\-': \\/.!$?]+|\"[^\"]*\"")
arxiu = io.open("C:\\Users\\Usuario\\Desktop\\Marvel_DC.csv",
                "r", encoding='utf-8')

llistadecadenes = [cadena.replace(",,", ",ND,")
                   for cadena in arxiu.readlines()]

matriu = []

for cadena in llistadecadenes:
    matriu.append(patro.findall(cadena))
for X in matriu:  # X = l'element que volem analitzar
    print(X)
    # time.sleep(1)
