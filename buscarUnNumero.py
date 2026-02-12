# Dado un array con números, revisa si el número 7 está dentro.


numeros = [3, 7, 2]
indice = 0

while indice < len(numeros):
    if numeros[indice] == 7:
        print("Si hay siete")
        break
    else:
        print("No hay siete")
        indice += 1
