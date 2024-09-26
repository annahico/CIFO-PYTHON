# 20. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les mateixes cadenes invertides.

def inversio_llista(llista):
    llista_invertida = []
    for cadena in llista:
        llista_invertida.append(cadena[::-1])  # inverteix la cadena utilitzant la sintaxi [::-1]
    return llista_invertida

llista = ['hola', 'com', 'estas']
print(inversio_llista(llista))
