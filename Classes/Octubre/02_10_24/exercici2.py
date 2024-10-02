# B) fila de files o matrius ✔️

# Matriu inicial
matriu = [[2, 3, "hola", 24, 34000, "hola2"], []]

# Accés a elements individuals
print(matriu[0][0])
print(matriu[0][2])

matriu[1].extend([5, 6, 7])  # Afegim elements a la segona fila
print(matriu)

# Recórrer la matriu
for fila in matriu:
    print(fila)
