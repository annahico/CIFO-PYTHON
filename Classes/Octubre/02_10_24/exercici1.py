# A) llista strings

["2, 3, hola, 24, 34.000, hola2 \n", "3,4, hola, 24, 54.000, hola3, \n",
    "3,4, hola, 24, 54.000, hola3\n", "3,4, hola3"]

# cadena = "2, 3, hola, 24, 34.000, hola2 \n"

# patro = re.compile("[a-z0-9\\.]+")
# patro.findall(cadena)

# --> elimimar els . de milers ✔️
# --> espais davant i darrere
# --> eliminar \n final de cada string ✔️
# --> split per la coma "," ✔️

cadena = "2, 3, hola, 24, 34.000, hola2 \n"

llista = cadena.replace(" ", "").replace(".", "").replace(
    "\n", "").split(",")
print(llista)
# ---------------------------------------------------------------------------------------------------


def string_to_list(cadena):
    for caracter in ".\n":
        cadena = cadena.replace(caracter, "")
    cadena = cadena.split(",")
    return cadena


llistastrings = ["2, 3, hola, 24, 34.000, hola2 \n", "3,4, hola, 24, 54.000, hola3, \n",
                 "3,4, hola, 24, 54.000, hola3\n", "3,4, hola3"]
# resultat = []
# for cadena in llistastrings:
#     for caracter in ".\n":
#         cadena = cadena.replace(caracter, "")
#     cadena = cadena.split(",")
#     resultat.append(cadena)
resultat = [cadena.replace(" ", "").replace(".", "").replace(
    "\n", "").split(",")for cadena in llistastrings]
print(resultat)
# ---------------------------------------------------------------------------------------------------
