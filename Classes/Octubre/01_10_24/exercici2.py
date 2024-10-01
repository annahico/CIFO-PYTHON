llistadellistes = [['hola', 'pepe', 'com', 'estas'],
                   ['la', 'farola', 'de', 'laredo']]


def quitarprimeraletra(l):
    resultat = []
    for sublista in l:
        temp = []
        for element in sublista:
            temp.append(element[1:])
        resultat.append(temp)


llistadellistes = [['hola', 'pepe', 'com', 'estas'],
                   ['la', 'farola', 'de', 'laredo']]

print(quitarprimeraletra(llistadellistes))
print(llistadellistes)
