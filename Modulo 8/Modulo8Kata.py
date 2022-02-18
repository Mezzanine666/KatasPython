#Ejercicio 1

planeta = {
    'name': 'Marte',
    'moons': 2
}
print(f'{planeta["name"]} tiene {planeta["moons"]} lunas')


planeta['circunferencia (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(f'{planeta["name"]} tiene una circunferencia polar de {planeta["circunferencia (km)"]["polar"]}')

#Ejercicio 2
lunas_en_planetas = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5
}

lunas = lunas_en_planetas.values()
planetas = len(lunas_en_planetas.keys())
total_lunas = 0
for luna in lunas:
    total_lunas = total_lunas + luna
promedio = total_lunas / planetas
print(f'El promedio de lunas es : {promedio}' )
