# Dado un array con 3 números, calcula la suma de todos.


numeros = [4, 8, 5]
i = 0
suma = 0

while i < len(numeros):
    suma = numeros[i] + suma
    i += 1

print(suma)
