# 7. Funció que pren com a paràmetre una llista de números i retorna la llista en ordre invertit.

def invertir_llista(llista):
    llista.reverse()  # Inverteix l'ordre de la llista
    return llista

llista = [4, 3, 2, 1, 8]
llista = invertir_llista(llista)  # Inverteix l'ordre de llista
print(llista)

l = [5, 4, 3, 2, 1]  # Nom de la nova llista
l = invertir_llista(l)  # Inverteix l'ordre de l
print(l)
