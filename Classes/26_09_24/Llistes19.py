# 19 Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les mateixes cadenes sense el primer caràcter.

def nofirst_llista(llista):
    nolast = []
    for cadena in llista:
        nolast.append(cadena[1:])  # Afegeix la cadena sense el primer caràcter
    return nolast

llista = ['hola', 'com', 'estas']
print(nofirst_llista(llista))
