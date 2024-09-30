llista = ['patates', 'llet', 'cocacola', 'patates', 'pizza', 'cocacola']

llista = list(set(llista))
print(llista)

# ------------------------------------------------------------------------------

llista = ['patates', 'llet', 'cocacola', 'patates', 'pizza', 'cocacola']

resultat = []  # creació d'una llista buida

for element in llista:  # Aquest bucle recorrerà cada element de LLISTA.
    # coprovem si l'element actual no es troba a la llista RESULTAT. Si no hi és, significa que NO hi han més
    if element not in resultat:
        # Si l'element és únic, s'afegeix a la llista RESULTAT.
        resultat.append(element)
print(resultat)

# ------------------------------------------------------------------------------

llista = ['patates', 'llet', 'cocacola', 'patates', 'pizza', 'cocacola']
resultat = []
[resultat.append(element) for element in llista if element not in resultat]
print(resultat)
