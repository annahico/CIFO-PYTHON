# 15. Jugar a endevinar un número

import random

numero_a_endevinar = random.randint(1, 100) # Es genera un número aleatori entre 1 i 100 mitjançant la funció randint(), i aquest número es guarda a la variable numero_a_endevinar
intent = 0 # questa variable s'utilitzarà per emmagatzemar cada intent de l'usuari.
print("Vols jugar a un joc? Adivina el número que estic pensant entre el 1 i el 100.")

while True: # Comença un bucle while infinit que continuarà fins que l'usuari endevini el número correcte.
    intent = int(input("Introdueix el teu intent: ")) # Es demana  que s'introdueixi un número , i aquest es converteix a enter i s'emmagatzema a la variable intent.
    if intent < numero_a_endevinar: # Es comprova si el número introduït per l'usuari és més petit que el número que ha generat l'ordinador.
        print("Maasa baix")
    elif intent > numero_a_endevinar: # Si l'intent no és menor, es comprova si és més gran que el número a endevinar.
        print("Massa alt.")
    else: # Aquesta part s'executa si cap de les condicions anteriors es compleix, ES CORRECTE
        print("¡Correcte! Pots continuar jugant si t'atreveixes.")
        break # trenca el buble quan encerta el número
