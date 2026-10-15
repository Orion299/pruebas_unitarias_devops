import pytest
from src.fibonacci import fibonacci_iterativo

def test_fibonacci_negativo_lanza_error():
    # Arrange
    n = -3
    # Act & Assert
    with pytest.raises(ValueError):
        fibonacci_iterativo(n)
