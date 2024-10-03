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


que_volem_analitzar = []

for X in matriu[1:]:  # X = l'element que volem analitzar
    que_volem_analitzar.append(int(X[0]))

    print(X)
