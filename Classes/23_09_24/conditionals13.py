# 17. Mostrar els n primers primers17. Mostrar els n primers primers

n = int(input("Introduce la cantidad de números primos a mostrar: "))
contador = 0
num = 2

while contador < n:
    es_primer = True
    i = 2
    while i <= num // 2:
        if num % i == 0:
            es_primer = False
            break
        i += 1
    if es_primer:
        print(num, end=' ')
        contador += 1
    num += 1
print()
