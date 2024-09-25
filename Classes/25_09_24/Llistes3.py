# 3. Funció que pren com a paràmetre una llista de números i retorna la suma dels quadrats dels seus elements.

def suma_elements(llista): # creació de les funcions
    suma = 0 # 
    for i in llista: # per cada element a la llista :
        suma += i * i # suma els quadrats

    return suma

llista1 = [4,3,2,1,8] # posem la llista 1
llista2 = [5,4,3,2,1] # posem la llista 2

print(suma_elements(llista1)) # imprimeix la llista 1
print(suma_elements(llista2)) # imprimeix la llista 2