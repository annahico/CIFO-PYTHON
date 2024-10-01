import re

# Definir el patró per a números enters
patro = re.compile(r"(?<!\S)-?[0-9]+(?!\S)")

# Sol·licitar la primera entrada
entrada = input("Escriu un número: ")

# Continuar demanant un número vàlid si no és correcte
while len(patro.findall(entrada)) != 1:
    entrada = input("Escriu un número vàlid: ")

# Obtenir el número validat
numero = patro.findall(entrada)[0]

# Condicions per determinar el signe del número
if numero == "0":
    print(f"El número que has escrit és {numero} i té un valor de 0.")
elif numero.isdigit():
    print(f"El nombre {numero} és positiu.")
elif "-" in numero:
    print(f"El nombre {numero} és negatiu.")
