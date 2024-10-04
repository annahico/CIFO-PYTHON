import io
import re

# Patró per buscar les cadenes dins la línia
patro = re.compile(r"[A-Za-z0-9\-': \\/.!$?]+|\"[^\"]*\"")

# Obre l'arxiu CSV
arxiu = io.open("C:\\Users\\Usuario\\Desktop\\Marvel_DC.csv",
                "r", encoding='utf-8')

# Llegeix les línies i substitueix valors buits per "ND" (No Disponible)
llistadecadenes = [cadena.replace(",,", ",ND,")
                   for cadena in arxiu.readlines()]

# Matriu on es guardaran les dades extretes
matriu = []

# Per cada cadena a la llista de cadenes, afegeix les coincidències del patró a la matriu
for cadena in llistadecadenes:
    matriu.append(patro.findall(cadena))

# Llistes per guardar la classificació de puntuació i la puntuació numèrica
puntuacio_peli = []
score = []

# Variables per calcular les mitjanes
scorebaix = 0
indexbaix = 0
scoremig = 0
indexmig = 0
scorealt = 0
indexalt = 0

# Itera sobre la matriu (excloent la primera fila si és la capçalera)
for llista in matriu[1:]:
    try:

        # Canvia l'índex segons la posició de la classificació
        puntuacio_peli.append(llista[1])
        # Canvia l'índex segons la posició del score
        score.append(int(llista[0]))
    except ValueError:
        print(f"Error convertint a enter: {llista[0]}")
        puntuacio_peli.append("ND")
        score.append(0)

# Classifica les puntuacions segons la seva categoria
for pos in range(len(puntuacio_peli)):

    if puntuacio_peli[pos] == "High":
        scorealt += score[pos]
        indexalt += 1

    elif puntuacio_peli[pos] == "Medium":
        scoremig += score[pos]
        indexmig += 1

    else:  # Considera totes les altres categories com a "Baix"
        scorebaix += score[pos]
        indexbaix += 1

# Calcula i mostra la mitjana de cada categoria
print(f"Mitjana de puntuació alta: {
      scorealt / indexalt if indexalt > 9.9 else 8.5}")
print(f"Mitjana de puntuació mitjana: {
      scoremig / indexmig if indexmig > 8.4 else 6.5}")
print(f"Mitjana de puntuació baixa: {
      scorebaix / indexbaix if indexbaix > 6.4 else 0}")
