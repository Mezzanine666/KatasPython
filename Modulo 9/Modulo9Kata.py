#Ejercicio 1

def informe(tanque1, tanque2, tanque3):
    promedio = (tanque1 + tanque2 + tanque3) / 3
    return f"""Informe: Promedio de tanques: {promedio}%
    Tanque1: {tanque1}%
    Tanque2: {tanque2}%
    Tanque3: {tanque3}% """
print(informe(60, 90, 40))

# Función promedio 
def promedio(valores):
    total = sum(valores)
    objetos = len(valores)
    return total / objetos

print(promedio([60, 65, 50])) 

def informe(tanque1, tanque2, tanque3):
    return f"""Fuel Report:
    Promedio total: {promedio([tanque1, tanque2, tanque3])}%
    Tanque1: {tanque1}%
    Tanque2: {tanque2}%
    Tanque3: {tanque3}% 
    """

print(informe(88, 76, 70))

#Ejericio 2
def reporte(prelanzamiento, tiempovuelo, destino, tanque_externo, tanque_interno):
    return f""" Mision a {destino}
    Tiempo de viaje: {prelanzamiento + tiempovuelo} minutos
    Combustible total: {tanque_externo + tanque_interno} galones """

print(reporte(90, 90, "Saturno", 6000, 1000))


def reporte(destino, *minutos, **combustible_reservado):
    return f""" Mision a {destino}
    Tiempo de viaje: {sum(minutos)} minutos
    Combustible total: {sum(combustible_reservado.values())} galones """

print(reporte("Saturno", 90, 90, 90, 90, interno=5500, externo=2000))


def reporte(destino, *minutos, **combustible_reservado):
    reporte_completo = f""" Mision a {destino}
    Tiempo de viaje: {sum(minutos)} minutos
    Combustible total: {sum(combustible_reservado.values())}
    """
    for tanque1, galones in combustible_reservado.items():
        reporte_completo += f"{tanque1} tanque -> {galones} galones reservados\n"
    return reporte_completo

print(reporte("Satuno", 57, 246, principal=700, externo=300))