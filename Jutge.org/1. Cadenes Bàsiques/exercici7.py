# Feu un programa que compti el número d’aparicions d’un caràcter concret en una cadena.

# Entrada

# Cadena d’entrada i caracter de cerca amb un espai entre ells dos.

# Sortida Cadena de sortida amb la cadena i el número d’aparicions. El format de sortida es mostra en els exemples.

# Observació

# Recorda que en tots els exercicis on es demana una cadena a l’entrada fem cadena = input(""). A part, aquí per obtenir la cadena i el caracter farem aquestes línies de codi:

# cadena = input("")[cadena, caracter] = cadena.split()

# Obtenim així el valor de la cadena i el caracter a cercar


# Entrada
cadena = input("")

# Obtenim la cadena i el caràcter a cercar
[cadena, caracter] = cadena.split()

# Comptem el nombre d'aparicions del caràcter en la cadena
num_aparicions = cadena.count(caracter)

# Format de sortida
if num_aparicions == 1:
    print(f"El caràcter {caracter} apareix una vegada a la cadena {cadena}")
else:
    print(f"El caràcter {caracter} apareix {
          num_aparicions} vegades a la cadena {cadena}")
