import io
import re

patro = re.compile(r"[A-Za-z0-9\-': \\/.!$?]+|\"[^\"]*\"")
arxiu = io.open("fitxer",
                "r", encoding='utf-8')

llistadecadenes = [cadena.replace(",,", ",ND,")
                   for cadena in arxiu.readlines()]

matriu = []

for cadena in llistadecadenes:
    matriu.append(patro.findall(cadena))


hores_estudiades = []

score = []
for llista in matriu[1:]:
    hores_estudiades.append(int(llista[0]))
    score.append(int(llista[-1]))

scorebaix = 0
indexbaix = 0  # veure cuanta gent hi ha

scoremig = 0
indexmig = 0

scorealt = 0
indexalt = 0

scoreover = 0
indexover = 0

for pos in range(len(hores_estudiades)):

    if 0 <= hores_estudiades < 10:
        scorebaix += score[pos]
        indexbaix += 1
    elif 10 <= hores_estudiades < 20:
        scoremig += score[pos]
        indexmig += 1
    elif 20 <= hores_estudiades < 30:
        scorealt += score[pos]
        indexalt += 1
    else:
        scoreover += score[pos]
        indexover += 1

    print(scorebaix / indexbaix, scoremig/indexmig,
          scorealt/indexalt, scoreover/indexover)
