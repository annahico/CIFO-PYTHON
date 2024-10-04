import io
import re

patro = re.compile(r"[A-Za-z0-9-–áéíóú;&_': \[\]\/\.()!$?]+|\"[^\"]*\"")

arxiu = io.open("C:\\Users\\Usuario\\Desktop\\Marvel_DC.csv",
                "r", encoding='utf-8')


llistadecadenes = [cadena.replace(",,", ",ND,").replace('""', '')
                   for cadena in arxiu.readlines()]

# Es defineixen dues llistes buides, matriu per emmagatzemar les línies processades i longituds per guardar la longitud de cada línia.
matriu = []
longituds = []

# Aquí, el codi fa servir l'expressió regular per trobar patrons a cada línia del CSV. El resultat s'emmagatzema en matriu. També es guarda la longitud de cada línia en longituds. La primera línia processada es mostra amb print(matriu[0]).
for cadena in llistadecadenes:
    temp = patro.findall(cadena)
    matriu.append(temp)
    longituds.append(len(temp))
print(matriu[0])

# Es fa el mateix procés anterior una vegada més, trobant patrons amb l'expressió regular i afegint-los a matriu.
for cadena in llistadecadenes:
    matriu.append(patro.findall(cadena))

# Es defineixen dues llistes buides per emmagatzemar els gèneres i les puntuacions de les pel·lícules.
generes = []
score = []

# Aquí, es recorren les llistes a matriu (excloent la primera fila, que podria ser l'encapçalament). L'element 3 (gènere) i l'element 6 (puntuació) es guarden a les llistes corresponents. Si hi ha un error en convertir la puntuació a float, es mostra un missatge d'error
for llista in matriu[1:]:
    try:
        generes.append(llista[3])
        score.append(float(llista[6]))
    except ValueError:
        print(f"Error convertint a enter: {llista[6]}")
print("????????", len(matriu), len(generes), len(score))

# Es fa una llista única de gèneres amb set(), després es creen dues llistes: una per sumar les puntuacions totals de cada gènere (puntuacio) i una altra per comptar quantes vegades apareix cada gènere (comptador).
classify = list(set(generes))
# print(set(generes))
puntuacio = len(classify)*[0]
comptador = len(classify)*[0]

# Es recorren les primeres 3380 pel·lícules. Per cada pel·lícula, es busca l'índex del seu gènere a la llista classify. Es suma la puntuació de la pel·lícula a puntuacio[indice] i s'incrementa el comptador d'aquell gènere.
for pos in range(3380):
    indice = classify.index(generes[pos])
    puntuacio[indice] += score[pos]
    comptador[indice] += 1

# Finalment, es calcula la puntuació mitjana de cada gènere dividint la suma total de puntuacions pel nombre de pel·lícules d'aquell gènere. Es mostren els resultats amb un print.
for pos in range(len(puntuacio)):
    print(classify[pos], puntuacio[pos]/comptador[pos])
