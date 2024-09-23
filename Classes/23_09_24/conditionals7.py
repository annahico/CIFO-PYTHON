# Llegeix els quatre nombres que conformen una adreça IP, valida si és una IP correcta i ho escriu.


parts = []  # Inicialitzem una llista per emmagatzemar les parts de l'adreça IP.
count = 0   # Inicialitzem un contador a 0.

while count < 4:  # Continuem fins que tinguem 4 parts vàlides.
    part = input(f"Introdueix la part {count + 1} de l'adreça IP (0-255): ")
    if part.isdigit() and 0 <= int(part) <= 255:  # Validem que sigui un número entre 0 i 255.
        parts.append(part)  # Afegim la part vàlida a la llista. SI aquesta part està malament, va al
        count += 1  # Incrementem el contador.
    else:
        print("Part invàlida. Assegura't que sigui un número entre 0 i 255.")  # Missatge d'error. Les IP només arriben fins 255

# Unim les parts vàlides amb punts per formar l'adreça IP.
ip = ".".join(parts)
print("L'adreça IP és:", ip)  # Imprimim l'adreça IP resultant.
