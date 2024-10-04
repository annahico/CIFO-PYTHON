import io
import re

patro = re.compile(r"[A-Za-z0-9-–áéíóú;&_': \[\]\/\.()!$?]+|\"[^\"]*\"")

arxiu = io.open("C:\\Users\\Usuario\\Desktop\\Marvel_DC.csv",
                "r", encoding='utf-8')


llistadecadenes = [cadena.replace(",,", ",ND,").replace('""', '')
                   for cadena in arxiu.readlines()]


matriu = []
longituds = []
for cadena in llistadecadenes:

    temp = patro.findall(cadena)
    matriu.append(temp)
    longituds.append(len(temp))
print(matriu[0])


for cadena in llistadecadenes:
    matriu.append(patro.findall(cadena))

generes = []

score = []
'''
scorebaix = 0
indexbaix = 0
scoremig = 0
indexmig = 0
scorealt = 0
indexalt = 0
'''

for llista in matriu[1:]:
    try:
        generes.append(llista[3])
        score.append(float(llista[6]))
    except ValueError:
        print(f"Error convertint a enter: {llista[6]}")
print("????????", len(matriu), len(generes), len(score))
classify = list(set(generes))
# print(set(generes))
puntuacio = len(classify)*[0]
comptador = len(classify)*[0]

for pos in range(3380):
    indice = classify.index(generes[pos])
    puntuacio[indice] += score[pos]
    comptador[indice] += 1

for pos in range(len(puntuacio)):

    print(classify[pos], puntuacio[pos]/comptador[pos])

'''
    if mitjana_generes[pos] == "High":
        scorealt += score[pos]
        indexalt += 1

    elif mitjana_generes[pos] == "Medium":
        scoremig += score[pos]
        indexmig += 1

    else:
        scorebaix += score[pos]
        indexbaix += 1

# Calcular la mitjana fora del bucle
if indexbaix > 0:
    mitjana_baixa = scorebaix / indexbaix
else:
    mitjana_baixa = 0

if indexmig > 0:
    mitjana_mitjana = scoremig / indexmig
else:
    mitjana_mitjana = 0

if indexalt > 0:
    mitjana_alta = scorealt / indexalt
else:
    mitjana_alta = 0

print(mitjana_baixa, mitjana_mitjana, mitjana_alta)
'''
