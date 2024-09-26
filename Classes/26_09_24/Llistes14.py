# 14. Funció que pren com a paràmetre una llista de cadenes i retorna una única cadena amb tots els elements concatenats (Suma d'strings o cadenes).

def concadena_llista(llista): #FUNCIÓ

    return ''.join(llista)# no es deixa separació entre les comes perque estigui tot junt

llista = ['hola', 'com', 'estas']
print(concadena_llista(llista)) 
