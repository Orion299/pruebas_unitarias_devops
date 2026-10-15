from src.conversor import celsius_a_fahrenheit, metros_a_pies, kilogramos_a_libras
import pytest

def test_celsius_a_fahrenheit_positivo():
    # Arrange
    celsius = 25.0
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == 77.0

def test_celsius_a_fahrenheit_cero():
    # Arrange
    celsius = 0.0
    # Act
    resultado = celsius_a_fahrenheit(celsius)
    # Assert
    assert resultado == 32.0

def test_metros_a_pies_basico():
    # Arrange
    metros = 2.0
    # Act
    resultado = metros_a_pies(metros)
    # Assert
    assert round(resultado, 2) == 6.56

def test_kilogramos_a_libras_basico():
    # Arrange
    kg = 10.0
    # Act
    resultado = kilogramos_a_libras(kg)
    # Assert
    assert round(resultado, 2) == 22.05
import pytest
from src.fibonacci import fibonacci_iterativo

def test_fibonacci_negativo_lanza_error():
    # Arrange
    n = -3
    # Act & Assert
    with pytest.raises(ValueError):
        fibonacci_iterativo(n)
