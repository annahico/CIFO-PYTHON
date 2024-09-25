# 19. Calcular el factorial d'un número sencer positiu

n = int(input("Introduce un número: "))
factorial = 1
i = 1

if n == 0:
    factorial = 1
else:
    while i <= n:
        factorial *= i
        i += 1

print(f"El factorial de {n} es: {factorial}")

