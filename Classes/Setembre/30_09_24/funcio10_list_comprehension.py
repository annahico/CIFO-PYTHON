def digits_llista(llista):
    llista_resultat = []
    for i in range(len(llista)):
        llista_resultat.append(len(str(llista[i])))
    return llista_resultat


llista2 = [5, 4, 3, 2, 1]
llista1 = [4, 3, 2, 1, 8]

print(digits_llista(llista1))
print(digits_llista(llista2))


# List Comprehension

def digits_llista(llista):

    return [len(str(llista[i])) for i in range(len(llista))]


def digits_llista_2(llista):
    return [len(str(element))for element in llista]


llista2 = [54, 4, 3, 2, 1]
llista1 = [43, 3, 2, 1, 8]

print(digits_llista(llista1))
print(digits_llista_2(llista2))
