'''
cadena.replace(caracter1,caracter2,caracter3)
cadena.strip(caracter) ---- tres
cadena.lstrip(caracter1) --- 
cadena.zfill(longitud desitjada)
fins que la longitud és la desitjada
'''

# cadena = input("Entra el nom")
# while not cadena.isalpha():
#     cadena = input("Introdueix bé el teu nom, pocasolta")

# print ("El teu nom és " + cadena)



def essencer(cadena):
    for lletra in cadena:
        if lletra not in "1234567890":
            return False
        return True
    
    print(essencer("1234567890"))


def esdecimal(cadena):
    if cadena.count('.') ==1:
        cadena = cadena.replace('.','')
        if essencer(cadena):
            return False
        return False
    
    print(esdecimal("12345234234."))