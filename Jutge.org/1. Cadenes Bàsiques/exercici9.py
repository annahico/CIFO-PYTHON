# Feu un programa que doni com a resultat l’index o posició de l’última aparició d’un caràcter a una cadena. Si el caràcter no apareix ens dirà un missatge personalitzat avisant de la no aparició.

# Entrada

# Cadena d’entrada i caràcter de cerca amb un espai entre ells dos.

# Sortida Missatge personalitzat amb la posició trobada o avís de què el caràcter no es troba a la cadena.

# Observació

# Recorda que en tots els exercicis on es demana una cadena a l’entrada fem cadena = input(""). A part, aquí per obtenir la cadena i el caràcter farem aquestes línies de codi:

# cadena = input("") i [cadena,caracter] = cadena.split()


# Entrada
cadena = input("")

# Obtenim la cadena i el caràcter a cercar
[cadena, caracter] = cadena.split()

# Busquem la posició de l'última aparició del caràcter
index = cadena.rfind(caracter)

# Format de sortida
if index != -1:
    print(f"El caràcter {caracter} apareix per última vegada a la posició {
          index} a la cadena {cadena}")
else:
    print(f"El caràcter {caracter} no es troba a la cadena {cadena}")
