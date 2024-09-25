# 11.Escriure tots els divisors d'un número en ordre ascendent

num = int(input("Introdueix un número: "))
i = 1 # S'inicialitza una variable i amb el valor 1. Aquesta variable s'utilitzarà per comprovar els divisors del número.

print(f"Divisors de {num}:")
while i <= num: # Comença un bucle while que s'executa mentre i sigui menor o igual que el valor de num. Aquest bucle s’utilitza per provar cada número entre 1 i num com a possible divisor.
    if num % i == 0: # Comprova si num és divisible per i. Si aquesta condició es compleix, significa que i és un divisor de num.
        print(i, end=' ') # Si i és un divisor de num, es mostra i per pantalla. 
    i += 1 # Incrementa el valor de i en 1, per provar el següent número com a possible divisor en la següent iteració del bucle.
print() #  salt de línia al final de la llista de divisors
