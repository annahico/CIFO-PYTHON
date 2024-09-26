# 5. Funció que pren com a paràmetre una llista de números i retorna el seu valor mínim.

def valor_min(llista_num):
    return(min(llista_num)) # aqui realitzem la resta de la llista1
llista_num1 = [4,3,2,1,8] # aqui s'indica el calor de la llista
print(valor_min(llista_num1))

def valor_min2(llista_num2):
    return(min(llista_num1)) # aqui realitzem la resta de la llista2
llista_num2 = [5,4,3,2,1] # aqui s'indica el calor de la llista
print(valor_min2(llista_num2))

# -------------------------------------------------------------------------------------------------

def valor_min_anna(llista_num): # aqui s'ordena la llista i després resta tot
    llista_num.sort() # aqui s'ordena la llista
    return llista_num[0] # aqui es realitza la resta

llista_num1 = [4,3,2,1,8]
llista_num2 = [5,4,3,2,1]

print(valor_min_anna(llista_num1))
print(valor_min_anna(llista_num2))


# ----------------------------------------------------------------------------------------------------

def minim(l):
    minim = l[0]
    for num in l[1:]:
        if num < minim:
            minim = num
    return minim

original = [-11,13,1,25]
print(minim(original))