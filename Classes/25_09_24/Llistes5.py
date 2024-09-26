# 5. Funció que pren com a paràmetre una llista de números i retorna el seu valor mínim.

def valor_min(llista_num):
    return(min(llista_num)) # aqui realitzem la resta de la llista1
llista_num = [4,3,2,1,8] # aqui s'indica el calor de la llista
print(valor_min(llista_num))

def valor_min2(llista_num2):
    return(min(llista_num)) # aqui realitzem la resta de la llista2
llista_num2 = [5,4,3,2,1] # aqui s'indica el calor de la llista
print(valor_min2(llista_num2))



def valor_min_anna(llista_num): # aqui s'ordena la llista i després resta tot
    llista_num.sort() # aqui s'ordena la llista
    return llista_num[0] # aqui es realitza la resta
print(valor_min_anna(llista_num))
print(valor_min_anna(llista_num2))


