# 18. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les mateixes cadenes sense l'últim caràcter

def nolast_llista(llista): #FUNCIÓ
    for posicio in range(len(llista)):
        llista[posicio] = llista[posicio][0:len(llista[posicio])-1]
    return (llista) # 

llista = ['hola', 'com', 'estas']
print(nolast_llista(llista)) 

