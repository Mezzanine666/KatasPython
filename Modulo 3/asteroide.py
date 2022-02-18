# asteroide.py
velocidad = 49
if velocidad > 20:
    print('¡Alerta! ¡Un asteroide se acerca a velocidades peligrosas!')
else:
    print('Sigue con tu día!')

velocidad1 = 19
if velocidad1 > 20:
    print('Hay una luz mágica en el cielo!')
elif velocidad1 == 20:
    print('Hay una luz mágica en el cielo!')
else:
    print('Nada que ver aquí!')

asteroide = 60
tamaño = 40
if asteroide > 25 and tamaño > 25:
    print('Alerta, Un asteroide muy peligroso viene hacia la Tierra!')
elif asteroide >= 20:
    print('Hay una luz en el cielo!')
elif tamaño < 25:
    print('Nada que ver aquí')
else:
    print('Nada que ver aquí')