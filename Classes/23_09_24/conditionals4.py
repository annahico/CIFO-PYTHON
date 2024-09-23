while True: # aixi no utilitzem el regex
    
    try:
        numero = int(input("Escriu un número: "))  # entra en bucle fins que sigui correcte
        break  # quan es correcte el número trenca el bucle
    except ValueError:
        print("Entrada Errònia, torna-hi")  # torna a demanar el número si es erroni

# Condicions per determinar el signe del númeror
if numero == 0:
    print(f"El número que has escrit és {numero} i té un valor de 0.")
elif numero > 0:
    print(f"El nombre {numero} és positiu.")
else:
    print(f"El nombre {numero} és negatiu.")
