import io
import re

# Patró per buscar les cadenes dins la línia
patro = re.compile(r"[A-Za-z0-9-–áéíóú;&_': \[\]\/\.()!$?]+|\"[^\"]*\"")
# Obre l'arxiu CSV
arxiu = io.open("C:\\Users\\Usuario\\Desktop\\Marvel_DC.csv",
                "r", encoding='utf-8')

# Llegeix les línies i substitueix valors buits per "ND" (No Disponible)
llistadecadenes = [cadena.replace(",,", ",ND,").replace('""', '')
                   for cadena in arxiu.readlines()]

# Matriu on es guardaran les dades extretes
matriu = []
longituds = []
# Per cada cadena a la llista de cadenes, afegeix les coincidències del patró a la matriu
for cadena in llistadecadenes:

    # analitzem la longitud  de la llista (quants apartats té en total)
    temp = patro.findall(cadena)
    matriu.append(temp)
    longituds.append(len(temp))
print(matriu[0])

score = []

#  Itera sobre la matriu (excloent la primera fila si és la capçalera)
for llista in matriu[1:]:
    try:

        # no possem INT perque es FLOAT perque es un camp numèric (5.4, 7.5)
        # analitzem la part 6 de la llista on surt les puntuacions
        score.append(float(llista[6]))
    except ValueError:
        print(f"Error convertint a enter: {llista[6]}")


print(sum(score)/len(matriu))
