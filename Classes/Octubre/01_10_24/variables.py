# VARIABLES LOCALES Y GLOBALES

def afegeix1(numero):
    numero.append(1)


numero = [5]
afegeix1(numero)
print(numero)

# ---------------------------------------------------------------------------------------------------
# VARIABLE GLOBLAL


def afegeix1():  # no cal possar la variable
    global numero
    numero.append(1)  # la funció enten la variable


numero = [5]
afegeix1()
print(numero)

# ---------------------------------------------------------------------------------------------------
