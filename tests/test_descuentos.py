from src.descuentos import calcular_descuento
import pytest

def test_calcular_descuento_normal():
    # Arrange
    precio = 100.0
    porcentaje = 20.0
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == 80.0

def test_calcular_descuento_cero():
    # Arrange
    precio = 200.0
    porcentaje = 0.0
    # Act
    resultado = calcular_descuento(precio, porcentaje)
    # Assert
    assert resultado == 200.0

def test_calcular_descuento_invalido_lanza_error():
    # Arrange / Act / Assert
    with pytest.raises(ValueError):
        calcular_descuento(100.0, -10.0)
