# 17. Mostrar els n primers primers17. Mostrar els n primers primers

numero = int(input("Introdueix la cantidat de números primers a mostrar: "))
contador = 0
num = 2 # Es defineix la variable num amb el valor 2, que és el primer número primer. Aquesta variable s'incrementarà per provar els següents números si són primers.

while contador < numero: # Comença un bucle while que continuarà fins que s'hagin trobat I mostrat NUMEROS números primers.
    es_primer = True # S'assumeix inicialment que NUM és un número primer
    i = 2 # Aquesta variable s'utilitza per comprovar si NUM té algun divisor.
    while i <= num // 2: # Aquest bucle while comprova si NUM té divisors entre 2 i la seva meitat (num // 2).
        if num % i == 0: # Comprova si NUM és divisible per i.
            es_primer = False # Si es troba un divisor s'indica que no es primer
            break
        i += 1 # Incrementa el valor de i en 1 per provar el següent número com a divisor de num en la següent iteració.
    if es_primer: #  despres de sortir del bucle, es comprova si no s'ha trobat cap divisor.
        print(num, end=' ')
        contador += 1 # Incrementa el contador perquè s'ha trobat un número primer més.
    num += 1 # Incrementa num per provar el següent número en la propera iteració.
print()
