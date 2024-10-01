# 19. Calcular el factorial d'un número sencer positiu

numero = int(input("Introdueix un número: "))
factorial = 1 # S’inicialitza la variable factorial amb el valor 1. Aquesta variable s’utilitzarà per calcular el factorial del número.
i = 1

if numero == 0: # Comprova si el número introduït és 0
    factorial = 1 # Si el número és 0, el programa assigna 1 a factorial (ja que 0! = 1).
else:
    while i <= numero: # Inicia un bucle while que s'executa mentre i sigui menor o igual al número introduït.
        factorial *= i # Es va acumulant la multiplicació de tots els nombres des de 1 fins a numero.
        i += 1 # Incrementa i en 1 per continuar amb el següent valor en la propera iteració.

print(f"El factorial de {numero} es: {factorial}")

