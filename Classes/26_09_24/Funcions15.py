# 15. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les mateixes cadenes ordenades en ordre alfabètic.

def ordena_llista(llista):
    llista_ordenada = sorted(llista, key=lambda cadena: cadena.lower()) # ordena la llista utilitzant key=lambda cadena: cadena.lower() per garantir que la comparació sigui insensible a majúscules i minúscules.
    return llista_ordenada

llista = ['hola', 'com', 'estas']

print(ordena_llista(llista))
