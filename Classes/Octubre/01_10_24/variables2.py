def afegeix2():
    global numero
    numero = 7


def afegeix1():
    numero = 1


numero = 5

afegeix1()
afegeix2()
print(numero)

# ---------------------------------------------------------------------------------------------------


def afegeix2(n):
    n += 7
    return n


def afegeix1(n):
    n += 1
    return n


numero = 5

numero = afegeix1(numero)
numero = afegeix2(numero)
print(numero)

# ---------------------------------------------------------------------------------------------------


def afegeix2(n):
    n += [7]  # LLISTA no es modifica
    return n


def afegeix1(n):
    n += [1]
    return n


numero = [5]

numero = afegeix1(numero)
numero = afegeix2(numero)
print(numero)

# ---------------------------------------------------------------------------------------------------


def afegeix2(n):
    n += "7"  # STRING es queda igual
    return n  # es posa RETURN o GLOBAL(millor return) per modificar


def afegeix1(n):
    n += "1"
    return n


n = "5"

n = afegeix1(n)
n = afegeix2(n)
print(n)
