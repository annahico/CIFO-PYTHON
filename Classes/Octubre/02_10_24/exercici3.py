import re
import time

patro = re.compile("[a-z0-9\.]+")  # Regex
llistastrings = []
# -------------------------------------------------------------------------------

for contador in range(1000):
    llistastrings.append("2,3,hola,24,34.000,hola2,\n")
inicial = time.time()
llistastrings = []
# print(llistastrings)

# resultat = []
# for cadena in llistastrings:
#     cadena = cadena.replace(".", "").replace("\n", "").split(",")
#     resultat.append(cadena)
# -------------------------------------------------------------------------------

# resultat = [cadena.replace(" ", "").replace(".", "").replace(
#     "\n", "").split(",")for cadena in llistastrings]

final = time.time()

print(f"tiempo total {final - inicial}")
