import io
import re
import time

inicial = time.time()

patro = re.compile(r"[A-Za-z0-9-–áéíóú;&_': \[\]\/\.()!$?]+|\"[^\"]*\"")

arxiu = io.open("C:\\Users\\Usuario\\Desktop\\Marvel_DC.csv",
                "r", encoding='utf-8')


llistadecadenes = [cadena.replace(",,", ",ND,").replace(
    '""', '') for cadena in arxiu.readlines()]


matriu = []

longituds = []

for cadena in llistadecadenes[1:]:

    temp = patro.findall(cadena)

    matriu.append(temp)

    longituds.append(len(temp))

generes = []

score = []

for llista in matriu:

    try:

        generes.append(llista[3])

        score.append(float(llista[6]))

    except ValueError:

        print("Error convertint a enter: ", llista[6])


classify = list(set(generes))

puntuacio = len(classify)*[0]

comptador = len(classify)*[0]

for pos in range(len(generes)):

    indice = classify.index(generes[pos])

    puntuacio[indice] += score[pos]

    comptador[indice] += 1

for pos in range(len(puntuacio)):

    print(classify[pos], puntuacio[pos]/comptador[pos])

final = time.time()

print(final - inicial)
