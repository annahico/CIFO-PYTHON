# Escriu una funció de Python per comprovar si una cadena és un pangrama o no.

# Nota: Els pangrames són paraules o frases que contenen cada lletra de l' alfabet almenys una vegada.

# Per exemple la frase en anglès : "The quick brown fox jumps over the lazy dog" és un pangrama.

# 5

# ..................
# ..................
# return ...........

# Per exemple,

# print(pangrama("The quick brown fox jumps over the lazy dog")) imprimirà a la pantalla True ja que la cadena és un pangrama.
# print(pangrama("Aquesta no es pangrama")) imprimirà a la pantalla False ja que la cadena no és un pangrama.
# NOTA. Les cadenes entrades seran sense accents per facilitar la feina.


import string


def pangrama(cadena):
    # Comprova si una cadena és un pangrama.
    # Convertim la cadena a minúscules i eliminem espais
    cadena = cadena.lower()
    # Creem un conjunt amb totes les lletres de l'alfabet
    alfabet = set(string.ascii_lowercase)
    # Creem un conjunt amb les lletres de la cadena
    lletres_cadena = set(cadena)
    # Comprovem si el conjunt de lletres de la cadena conté totes les lletres de l'alfabet
    return alfabet.issubset(lletres_cadena)


print(pangrama("The quick brown fox jumps over the lazy dog"))  # Imprimirà True
print(pangrama("Aquesta no es pangrama"))  # Imprimirà False
