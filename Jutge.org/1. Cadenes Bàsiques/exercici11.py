# Feu un programa que doni com a resultat una cadena amb les paraules d’una llista.

# Entrada

# Paraules separades per coma i sense espais.

# Sortida Llista amb les paraules.

# Observació

# Recorda que en tots els exercicis on es demana una cadena a l’entrada fem cadena = input(""). A part, aquí per obtenir la cadena i el caràcter farem aquestes línies de codi:

# cadena = input("") i també utilitzarem el mètode de cadenes split(’,’).


# Entrada
cadena = input("")

# Converteix la cadena d'entrada en una llista de paraules
paraules = cadena.split(',')

# Uneix les paraules en una cadena sense espais
resultat = ''.join(paraules)

# Mostra la cadena resultant
print(resultat)
