# 1. Funció que pren com a paràmetre una llista de números i retorna una altra llista ordenada.
def ordena_llista(lista): # Defineix una funció ordena_llista que rep un paràmetre, lista.
    llista.sort()  # ordenar la llista original
    return llista # el valor que la funció ha de retornar

llista = [4, 3, 2, 1, 8]
print(ordena_llista(llista))


# 2. Funció que pren com a paràmetre una llista de números i retorna la suma dels seus elements.
def suma_elements(llista): # creació de les funcions
    suma = 0 #  s'utilitza per acumular la suma dels elements de la llista. S'initia a 0 perquè és el valor neutre per a l'operació de suma.
    for i in llista: # per cada element a la llista :
        suma += i # suma un element darrere de cada element de la llista
    return suma


# 3. Funció que pren com a paràmetre una llista de números i retorna la suma dels quadrats dels seus elements.
def suma_elements(llista): # creació de les funcions
    suma = 0 # 
    for i in llista: # per cada element a la llista :
        suma += i * i # suma els quadrats x2
    return suma


# 4. Funció que pren com a paràmetre una llista de números i retorna la suma dels cubs dels seus elements.
def suma_elements(llista): # creació de les funcions
    suma = 0 # 
    for i in llista: # per cada element a la llista :
            suma += i ** 3 # realitza la multiplicació més fàcil
            # suma += i * i * i    # suma els quadrats x3
    return suma


# 5. Funció que pren com a paràmetre una llista de números i retorna el seu valor mínim.
def minim(l):
    minim = l[0]
    for num in l[1:]: # Comença un bucle que itera sobre cada element de la llista, començant des del segon element (l'índex 1) fins a l'últim
        if num < minim: # comprova si l'element actual num és menor que el valor actual de minim.
            minim = num # Si la condició és certa, actualitza la variable minim amb el nou valor num.
    return minim


# 6. Funció que pren com a paràmetre una llista de números i retorna el seu valor màxim.
def maxim(l):
    maxim = l[0]
    for num in l[1:]:
        if num > maxim: # comprova si l'element actual num és major que el valor actual de màxim.
            maxim = num # Si la condició és certa, actualitza la variable major amb el nou valor num.
    return maxim


# 7. Funció que pren com a paràmetre una llista de números i retorna la llista en ordre invertit.
def invertir_llista(llista):
    llista.reverse()  # Inverteix l'ordre de la llista
    return llista


# 8. Funció que pren com a paràmetre una llista de números i retorna una altra llista amb els elements en posició parell.
def parell(l):
    resultat = []
    for posicio in range(0,len(l),2): # Utilitza un bucle per recórrer només les posicions parells de la llista.
        resultat.append(l[posicio]) # Afegeix cada element de les posicions parells a resultat mitjançant append().
    return resultat


# 9. Funció que pren com a paràmetre una llista de números i retorna una altra llista amb els elements en posició senar.
def imparell(l):
    resultat = []
    for posicio in range(1,len(l),2): # Utilitza un bucle per recórrer només les posicions imparells de la llista.
        resultat.append(l[posicio]) # Afegeix cada element de les posicions parells a resultat mitjançant append().
    return resultat


# 10. Funció que pren com a paràmetre una llista de números i retorna una altra llista amb el número de dígits de cada element.
def digits_llista(llista):
    llista_resultat = []
    for i in range(len(llista)):
        llista_resultat.append(len(str(llista[i]))) # afegeixo la longitut (indicant que es un string) de la llista i quants digits hi han en cada element (I)
    return llista_resultat


# 11. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb la longitud de cadascuna de les cadenes que formen la llista.
def longitud_llista(llista):
    llista_resultat = []
    for i in range(len(llista)): # itera sobre els índexs de la llista, permetent accedir a cada element mitjançant el seu índex.
        llista_resultat.append(len(str(llista[i]))) #  calcula la longitud de l'element en la posició i de llista (convertit a cadena) i l'afegeix a llista_resultat.
    return llista_resultat


# 12. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les mateixes cadenes en minúscules.
def minus_llista(llista):
    llista_resultat = []
    for i in range(len(llista)):
        llista_resultat.append((str(llista[i].lower()))) # funció de cadenes, hem de convertir la llista i el I en cadena
    return llista_resultat


# 13. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les mateixes cadenes en majúscules.
def mayus_llista(llista):
    llista_resultat = []
    for i in range(len(llista)):
        llista_resultat.append((str(llista[i].upper()))) # funció de cadenes, hem de convertir la llista i el I en cadena
    return llista_resultat


# 14. Funció que pren com a paràmetre una llista de cadenes i retorna una única cadena amb tots els elements concatenats (Suma d'strings o cadenes).
def sumastrings(l): 
    resultado = "" # Inicialitza una cadena buida que s'utilitzarà per acumular les cadenes concatenades.
    for cadena in l: # Comença un bucle que itera sobre cada element cadena de la llista l.
        resultado += cadena # Afegeix cada cadena de la llista a resultado mitjançant l'operador +=, que concatena les cadenes.
    return resultado


# 15. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les mateixes cadenes ordenades en ordre alfabètic.
def ordena_llista(llista):
    llista_ordenada = sorted(llista, key=lambda cadena: cadena.lower()) # ordena la llista utilitzant key=lambda cadena: cadena.lower() per garantir que la comparació sigui insensible a majúscules i minúscules.
    return llista_ordenada


# 16. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les cadenes que es troben en posició parell.
def parelles(llista): 
    llista_resultat = [] 
    for i in range(len(llista)): # El codi recorre cada índex de la llista llista (i= index)
        if i % 2 == 0: #  El codi comprova si I és un nombre parell. utilitza l'operador de mòdul (%), que retorna el residu de dividir i per 2. Si el residu és zero (== 0), vol dir que i és parell, i la condició es compleix.
            llista_resultat.append(llista[i]) # Afegeix l'element llista[i] a llista_resultat.
    return llista_resultat


# 17. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les cadenes que es troben en posició senar.
def parelles(llista): 
    llista_resultat = [] 
    for i in range(len(llista)): # El codi recorre cada índex de la llista llista (i= index)
        if i % 2 != 0: #  El  codi recorre cada element de la llista llista I verifica si és senar (i % 2 != 0), és a dir, si no és divisible per 2.
            llista_resultat.append(llista[i]) # Afegeix l'element llista[i] a llista_resultat.
    return llista_resultat


# 18. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les mateixes cadenes sense l'últim caràcter
def nolast_llista2(llista):
    nolast = []
    for cadena in llista:
        nolast.append(cadena[0:len(cadena)-1]) # recorre els elements de cada cadena i elimina l'últim caracter de cada cadena de la llista
    return (nolast)


# 19 Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les mateixes cadenes sense el primer caràcter.
def nofirst_llista(llista):
    nolast = []
    for cadena in llista:
        nolast.append(cadena[1:])  # Afegeix la cadena sense el primer caràcter
    return nolast


# 20. Funció que pren com a paràmetre una llista de cadenes i retorna una altra llista amb les mateixes cadenes invertides.
def inversio_llista(llista):
    llista_invertida = []
    for cadena in llista:
        llista_invertida.append(cadena[::-1])  # inverteix la cadena utilitzant la sintaxi [::-1]
    return llista_invertida





