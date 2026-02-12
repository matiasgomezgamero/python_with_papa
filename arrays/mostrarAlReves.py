# Dado un array con 4 números, muéstralos empezando desde el último.


numeros = [5, 3, 8, 6]
i = len(numeros) - 1

while i >= 0:
    print(numeros[i])
    i -= 1
