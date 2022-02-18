texto = """Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth.",
"On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""
texto_cortado = texto.split('. ')
print(texto_cortado)

palabras_clave = ["average", "temperature", "distace"]

for sentencia in texto_cortado:
    for clave in palabras_clave:
        if clave in sentencia:
            print(sentencia.replace(' C', ' Celsius'))
            break

planeta = 'Jupiter '
gravedad  = 0.01346
nombre = 'Calisto'
titulo = f'datos de gravedad sobre {nombre}'
print(titulo)

datos = f"""{'-'*80} 
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 """

plantilla = f"""{titulo.title()} 
{datos} 
""" 
print(plantilla)

