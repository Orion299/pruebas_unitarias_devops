"""
Módulo con el algoritmo de Fibonacci.
"""

def fibonacci_iterativo(n):
    """Calcula el n-ésimo número de Fibonacci de forma iterativa."""
    if n < 0:
        raise ValueError("El índice no puede ser negativo")
    if n == 0:
        return 0

    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

def fibonacci_serie(n):
    """Genera una serie de Fibonacci hasta el n-ésimo término."""
    if n < 0:
        raise ValueError("El índice no puede ser negativo")

    if n == 0:
        return [0]

    if n == 1:
        return [0, 1]

    serie = [0, 1]
    for i in range(2, n + 1):
        siguiente = serie[i - 1] + serie[i - 2]
        serie.append(siguiente)

    return serie

def es_fibonacci(numero):
    """Verifica si un número es de Fibonacci."""
    if numero < 0:
        return False
    if numero == 0 or numero == 1:
        return True
    
    return es_cuadrado_perfecto(5 * numero * numero + 4) or \
           es_cuadrado_perfecto(5 * numero * numero - 4)

def es_cuadrado_perfecto(numero):
    """Verifica si un número es un cuadrado perfecto."""
    if numero < 0:
        return False
    raiz = int(numero ** 0.5)
    return raiz * raiz == numero
