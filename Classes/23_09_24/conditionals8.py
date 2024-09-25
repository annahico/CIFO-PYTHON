# Sumar les potències de 2 menors a 100

total = 0 # inicialitza la variable total amb un valor de 0, que serà utilitzada per emmagatzemar la suma de les potències de 2
numero = 1 # es defineix la variable numero, que comença amb el valor 1, la primera potència de 2 (2^0 = 1).

while numero < 100: # NUMERO menor a 100
    total += numero # suma el valor actual de numero a la variable total. Això vol dir que afegim la potència de 2 actual a la suma total.
    numero *= 2 # es multiplica el valor de numero per 2, generant la següent potència de 2.
print("La suma de les potències de 2 menors a 100 és:", total)
