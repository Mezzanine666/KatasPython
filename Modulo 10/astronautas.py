def agua_restante(astronautas, agua_restante, dias_restantes):
    for respuesta in [astronautas, agua_restante, dias_restantes]:
        try:
            respuesta / 10
        except TypeError:
       
            raise TypeError(f"All arguments must be of type int, but received: '{respuesta}'")
    dias = astronautas * 11
    uso_total = dias * dias_restantes
    agua_total_restante = agua_restante - uso_total
    if agua_total_restante < 0:
        raise RuntimeError(f"No hay suficiente agua para  {astronautas} astronautas después de {dias_restantes} dias!")
    return f"Agua total que queda después {dias_restantes} dias es: {agua_total_restante} litros"

print(agua_restante(3, 50, 2))

