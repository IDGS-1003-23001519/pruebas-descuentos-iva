import pytest

from calculadora import calcular_descuento, calcular_iva


def test_descuento_20_por_ciento():
    assert calcular_descuento(100, 20) == 80.00


def test_descuento_50_por_ciento():
    assert calcular_descuento(200, 50) == 100.00


def test_descuento_100_por_ciento():
    assert calcular_descuento(150, 100) == 0.00


def test_iva_16_por_ciento():
    assert calcular_iva(100) == 116.00


def test_iva_personalizado():
    assert calcular_iva(200, 10) == 220.00


def test_iva_con_redondeo():
    assert calcular_iva(10, 16) == 11.60


def test_precio_negativo_en_descuento():
    with pytest.raises(ValueError):
        calcular_descuento(-100, 20)


def test_iva_con_precio_negativo():
    with pytest.raises(ValueError):
        calcular_iva(-100)


def test_descuento_fuera_de_rango():
    with pytest.raises(ValueError):
        calcular_descuento(100, 120)
