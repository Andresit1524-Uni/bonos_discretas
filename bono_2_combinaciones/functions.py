"""functions contiene todas las funciones para el desarrollo del Bono 2 - Combinaciones. Incluye
algoritmos y funciones auxiliares para la entrada y salida de datos.

Los algoritmos incluyen verificaciones de tipo, porque resulta que las anotaciones de tipo en Python
son de adorno literalmente >:(
"""

import math as m
from typing import Optional


# region Algoritmos


def recursive_combination(n: int, k: int) -> int:
    """Calcula combinaciones de forma recursiva usando la regla de Pascal"""

    # Error de tipo si no son enteros
    if type(n) is not int or type(k) is not int:
        raise TypeError(f"Valores no válidos: {n}, {k}")

    # Error si alguno es menor que cero o si n es menor que k
    if n < 0 or k < 0 or n < k:
        raise ValueError(f"Valores no válidos: {n}, {k}")

    # Caso base
    if k == 0 or k == n:
        return 1

    # Recursión
    return recursive_combination(n - 1, k) + recursive_combination(n - 1, k - 1)


def pascal_triangle(n: int):
    """Imprime el triángulo de Pascal con n filas"""

    row = []
    for _ in range(n):
        # Crea la fila
        for i in range(len(row) - 1, 0, -1):
            row[i] = row[i] + row[i - 1]
        row.append(1)

        # Imprime la fila
        print("\t".join(str(x) for x in row))


# endregion
