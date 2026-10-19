def calcular_descuento(precio, porcentaje):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if not 0 <= porcentaje <= 100:
        raise ValueError("El descuento debe estar entre 0 y 100")

    descuento = precio * porcentaje / 100
    return round(precio - descuento, 2)

def calcular_iva(precio, porcentaje=16):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if not 0 <= porcentaje <= 100:
        raise ValueError("El IVA debe estar entre 0 y 100")

    iva = precio * porcentaje / 100
    return round(precio + iva, 2)
