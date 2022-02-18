distancia_tierra = 149597870
distancia_jupiter = 778547200

resta = distancia_jupiter - distancia_tierra
print(resta)

millas = resta * 0.621
print(millas)

planeta1 = input("Distancia del primer planeta en KM: ")
planeta1 = int(planeta1)
planeta2 = input("Distancia del segundo planeta en KM: ")
planeta2 = int(planeta2)

distancia = planeta2 - planeta1
print(distancia)

convertir_millas = distancia * 0.621
print(abs(convertir_millas))