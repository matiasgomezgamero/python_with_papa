# Crea un array con los nombres de 3 mascotas y que pregunte cual quiere mostrar.


mascotas = ["Nino", "Muñeca", "Teso"]

while True:
    respuesta = int(input("Numero de perro: ")) - 1

    if respuesta > len(mascotas) or respuesta < 0:
        print("Solo hay 3 perros")
    else:
        print(mascotas[respuesta])
        break
