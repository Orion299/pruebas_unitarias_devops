import pytest
from src.calculadora import dividir

def test_dividir_por_cero_lanza_error():
    # Arrange
    a = 10
    b = 0
    # Act & Assert
    with pytest.raises(ValueError):
        dividir(a, b)
