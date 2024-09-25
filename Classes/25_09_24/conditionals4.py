# 8. Calcular la mitjana dels números positius llegits

suma = 0 # Variable per emmagatzemar la suma dels números positius
contador = 0 # Variable per comptar quants números positius s'han llegit

while True:
    numero = int(input("Introdueix un número positiu: "))
    
    if numero < 0:  # Si el número és negatiu, es trenca el bucle i dona la mitjana
        break
    
    suma += numero # Suma el número introduït
    contador += 1  # Incrementa el comptador


if contador > 0:
    mitjana = suma / contador
    print(f"La mitjana dels números positius és: {mitjana}")
else:
    print("No s'han introduït números positius.")

