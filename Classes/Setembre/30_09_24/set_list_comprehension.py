llista = [1, 1, 3, 4, 4, 5]

# el SET imprimeix la llista aleatoriament en l'ordre aleatori
llista = list(set(llista))

print(llista)

# VERSIO 2
llista = [1, 1, 3, 4, 4, 5]
print(set(llista))  # aqui imprimeix entre claus {}


# VERSIO 3
llista = [1, 1, 3, 4, 4, 5]
colect = set(llista)
print(list(colect))
