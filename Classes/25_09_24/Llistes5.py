# 5. Funció que pren com a paràmetre una llista de números i retorna el seu valor mínim.

def valor_min(llista_num):
    return(min(llista_num))
llista_num = [4,3,2,1,8]
print(valor_min(llista_num))


def valor_min2(llista_num2):
    return(min(llista_num))
llista_num2 = [5,4,3,2,1]
print(valor_min2(llista_num2))


def valor_min_anna(llista_num):
    llista_num.sort()
    return llista_num[0]
print(valor_min_anna(llista_num))
print(valor_min_anna(llista_num2))


