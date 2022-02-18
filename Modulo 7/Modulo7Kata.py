#Ejercicio 1

new_planet = ''
planets = []

while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet = input('Ingresa el nombre de un planeta o bien si haz terminado escribe la palabra "done"')

#Ejercicio 2

for planet in planets:
    print(planet)