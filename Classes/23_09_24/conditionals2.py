import re

# Corrected pattern: 'compile', and match numbers with optional negative sign
patro = re.compile(r"-?[0-9]+")  #(r"(?<!\S)-?[0-9]+(?!\S)")

entrada = (input("Escriu un número: "))
    # print(patro.findall(entrada)) abans de continuar, fer un PRINT

while len(patro.findall(entrada)) != 1:
    entrada = (input("Escriu un número: "))

# Find all numbers in the input
print(patro.findall(entrada))

# Check if the input is zero, positive or negative
if entrada == "0":
    print(f"El número que has escrit és {entrada} i té un valor de 0")

elif entrada.isdigit():
    print(f"El nombre {entrada} és positiu")

elif entrada.startswith('-') and entrada[1:].isdigit():
    print(f"El nombre {entrada} és negatiu")
