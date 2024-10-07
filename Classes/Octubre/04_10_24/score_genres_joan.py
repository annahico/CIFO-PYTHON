import io
import re
import time
from collections import defaultdict

inicial = time.time()

# Compilació del patró regex
patro = re.compile(r"[A-Za-z0-9-–áéíóú;&_': \[\]\/\.()!$?]+|\"[^\"]*\"")

# Lectura del fitxer
with io.open("C:\\Users\\Usuario\\Desktop\\Marvel_DC.csv", "r", encoding='utf-8') as arxiu:
    llistadecadenes = [cadena.replace(",,", ",ND,").replace(
        '""', '') for cadena in arxiu.readlines()]

# Aplicació del patró a cada cadena
matriu = [patro.findall(cadena) for cadena in llistadecadenes[1:]]

# Diccionaris per emmagatzemar puntuacions totals i comptadors per cada gènere
puntuacions = defaultdict(float)
comptadors = defaultdict(int)


# Processament de cada llista
for llista in matriu:
    genere = llista[3]
    puntuacio = float(llista[6])
    puntuacions[genere] += puntuacio
    comptadors[genere] += 1

# Càlcul i impressió de la mitjana per gènere
for genere, total_puntuacio in puntuacions.items():
    print(f"{genere}: {total_puntuacio / comptadors[genere]}")

final = time.time()

print(final-inicial)
