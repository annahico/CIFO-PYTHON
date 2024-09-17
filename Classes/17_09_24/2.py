frase = input('Escriu una frase: ')
numero = input('Escriu un número: ')
repeticions = int(numero)

print(repeticions)
print((frase+'\n') * repeticions)
# \n es igual al numero = input


# opció 2

entrada = input('Escriu una frase: ')
num_repeticions = int(input('Escriu un número baix: '))
contador = 0

while contador < num_repeticions:
    print(entrada)
    contador += 1


# opció 3

frase = input ('Entra Frase')+ '\n'
repeticions = int(input('Entra repeticions'))

print(frase*repeticions)