#Ejercicio 1

planetas = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']
print('El sistema solar tiene', len(planetas), 'planetas')

planetas.append('Pluto')
print('El ultimo planeta del sistema solar es', planetas[-1])


#Ejercicio 2
planetas1 = ['Mercurio', 'Venus', 'Tierra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Neptuno']

nombre_planeta = input("Agrega el nombre del planeta utilizando la primer letra en Mayuscula: ")
planeta_index = planetas1.index(nombre_planeta)

print("Aquí están los planetas más cerca" + str(planeta_index))
print(planetas1[0:planeta_index])

print("Aquí están los planetas más lejos" + str(planeta_index))
print(planetas1[planeta_index + 1:])


