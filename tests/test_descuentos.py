from src.descuentos import calcular_descuento
import pytest

def test_descuento_normal():
    # Arrange
    precio, descuento = 100.0, 20.0
    # Act
    res = calcular_descuento(precio, descuento)
    # Assert
    assert res == 20.0

def test_descuento_cero():
    # Arrange
    precio, descuento = 50.0, 0.0
    # Act
    res = calcular_descuento(precio, descuento)
    # Assert
    assert res == 0.0

def test_descuento_limite_maximo():
    # Arrange
    precio, descuento = 100.0, 100.0
    # Act
    res = calcular_descuento(precio, descuento)
    # Assert
    assert res == 100.0

def test_descuento_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_descuento(100.0, -10.0)
