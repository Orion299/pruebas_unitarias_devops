from src.calculadora import sumar, restar, multiplicar, dividir
import pytest

def test_sumar_positivos():
    # Arrange
    a, b = 7, 5
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == 12

def test_sumar_negativos():
    # Arrange
    a, b = -3, -4
    # Act
    resultado = sumar(a, b)
    # Assert
    assert resultado == -7

def test_restar_positivos():
    # Arrange
    a, b = 10, 4
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == 6

def test_restar_negativos():
    # Arrange
    a, b = -7, -5
    # Act
    resultado = restar(a, b)
    # Assert
    assert resultado == -2

def test_multiplicar_positivos():
    # Arrange
    a, b = 3, 4
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 12

def test_multiplicar_cero():
    # Arrange
    a, b = 10, 0
    # Act
    resultado = multiplicar(a, b)
    # Assert
    assert resultado == 0

def test_dividir_positivos():
    # Arrange
    a, b = 10, 2
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 5

def test_dividir_decimales():
    # Arrange
    a, b = 5, 2
    # Act
    resultado = dividir(a, b)
    # Assert
    assert resultado == 2.5

def test_dividir_por_cero_lanza_error():
    with pytest.raises(ValueError):
        dividir(10, 0)
