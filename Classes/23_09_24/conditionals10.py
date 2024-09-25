# 11.Escriure tots els divisors d'un número en ordre ascendent

num = int(input("Introdueix un número: "))
i = 1

print(f"Divisors de {num}:")
while i <= num:
    if num % i == 0:
        print(i, end=' ')
    i += 1
print()
