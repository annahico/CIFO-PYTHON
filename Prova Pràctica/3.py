# 3. Escriure una funció que, donada un string, retorni la longitud de l'última paraula.
# Es considera que les paraules estan separades per un o més espais.
# També hi podria haver espais al principi o al final de l'string.

# def ultimalen(cadena)
# ..................
# ..................
# ..................
# return ...........

# Per exemple,
# print(ultimalen(“ Tinc tanta son que a les cinc tinc son ”)) imprimirà a la
# pantalla el número 3. ...... donat que 3 és la longitud de la última paraula son.


def ultimalen(cadena):
    # Eliminem espais al principi i al final, i separem la cadena per espais
    paraules = cadena.strip().split()
    # Si la llista de paraules no és buida, retornem la longitud de l'última paraula
    if paraules:
        return len(paraules[-1])
    else:
        return 0  # Si no hi ha paraules, retornem 0


print(ultimalen(" Tinc tanta son que a les cinc tinc son "))  # Imprimirà 3
