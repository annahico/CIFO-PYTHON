import io
import re

# Patró per buscar les cadenes dins la línia
patro = re.compile(r"[A-Za-z0-9-–áéíóú;&_': \[\]\/\.()!$?]+|\"[^\"]*\"")

# Obre l'arxiu CSV
arxiu = io.open("C:\\Users\\Usuario\\Desktop\\Marvel_DC.csv",
                "r", encoding='utf-8')

# Llegeix les línies i substitueix valors buits per "ND" (No Disponible)
llistadecadenes = [cadena.replace(",,", ",ND,").replace(
    '""', '') for cadena in arxiu.readlines()]

# Matriu on es guardaran les dades extretes
matriu = []
longituds = []

# Per cada cadena a la llista de cadenes, afegeix les coincidències del patró a la matriu
for cadena in llistadecadenes:
    temp = patro.findall(cadena)
    matriu.append(temp)
    longituds.append(len(temp))

    # Mostra la primera línia de la matriu
    print(matriu[0])

    # Comprova si la longitud és 9 i mostra la cadena i les coincidències
    if len(temp) == 9:
        print(cadena, temp)

# Mostra la longitud de les cadenes trobades
print(f"*********{set(longituds)}")
print(matriu[0])

# Compta quantes cadenes tenen cada longitud
for element in set(longituds):
    print(element, longituds.count(element))
