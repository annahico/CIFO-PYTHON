# 9. Dir si un número és primer o no

num = int(input("Introdueix un número: ")) # Es demana introduir un número enter i aquest es guarda a la variable num.
es_primer = True # Es defineix una variable es_primer com a True. Aquesta variable serà utilitzada per determinar si el número és primer o no.
i = 2 # S'inicialitza una variable i amb el valor 2. Aquesta variable s'utilitzarà com a divisor per comprovar si el número és divisible per altres números.

if num < 2: # Comprova si el número és menor que 2. Els nombres menors que 2 (és a dir, 0 i 1) no es consideren primers.
    es_primer = False # Si el número és menor que 2, es defineix es_primer com a False perquè aquests números no són primers.
else:
    while i <= num // 2: # El bucle while s'executa mentre i sigui menor o igual a la meitat del número (num // 2). No cal comprovar divisors més enllà de la meitat perquè cap número es divideix de manera sencera per un nombre més gran que la seva meitat.
        if num % i == 0: # Comprova si num és divisible per i. Si ho és, significa que num no és primer
            es_primer = False # Si num és divisible per i, es canvia es_primer a False, indicant que el número no és primer.
            break # surt del bucle
        i += 1 # Incrementa el valor de i en 1, per provar el següent possible divisor en la propera iteració del bucle.

if es_primer: # Després de sortir del bucle, es comprova el valor de es_primer.
    print(f"{num} és un número primer.")
else: # Si es_primer és False, això vol dir que s'ha trobat algun divisor del número.
    print(f"{num} no eés un número primer.")
