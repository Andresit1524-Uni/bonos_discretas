"""functions contiene todas las funciones para el desarrollo del Bono 2 - Combinaciones. Incluye
algoritmos y funciones auxiliares para la entrada y salida de datos.

Los algoritmos incluyen verificaciones de tipo, porque resulta que las anotaciones de tipo en Python
son de adorno literalmente >:(
"""


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


# Esta variable se considera persistente por módulos, por lo que si se llama varias veces su efecto
# de memoización se conserva
cached = {}


def memoized_combination(n: int, k: int) -> int:
    if (n, k) in cached:
        return cached[(n, k)]

    # Error de tipo si no son enteros
    if type(n) is not int or type(k) is not int:
        raise TypeError(f"Valores no válidos: {n}, {k}")

    # Error si alguno es menor que cero o si n es menor que k
    if n < 0 or k < 0 or n < k:
        raise ValueError(f"Valores no válidos: {n}, {k}")

    # Caso base
    if k == 0 or k == n:
        cached[(n, k)] = 1
        return 1

    # Recursión y caché
    result = memoized_combination(n - 1, k) + memoized_combination(n - 1, k - 1)
    cached[(n, k)] = result
    return result


def iterative_combination(n: int, k: int) -> int:
    """Calcula combinaciones de forma iterativa usando la fórmula desenrollada"""

    # Error de tipo si no son enteros
    if type(n) is not int or type(k) is not int:
        raise TypeError(f"Valores no válidos: {n}, {k}")

    # Error si alguno es menor que cero o si n es menor que k
    if n < 0 or k < 0 or n < k:
        raise ValueError(f"Valores no válidos: {n}, {k}")

    # Optimizamos usando la identidad de Pascal
    k = min(k, n - k)

    result: int = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) // i

    return result


def pascal_triangle(n: int):
    """Imprime el triángulo de Pascal con n filas"""

    # Error de tipo si no es un entero
    if type(n) is not int:
        raise TypeError(f"Valor no válido: {n}")

    # Error si es menor que cero
    if n < 0:
        raise ValueError(f"Valor no válido: {n}")

    row = []
    for _ in range(n):
        # Crea la nueva fila sobrescribiendo la anterior
        for i in range(len(row) - 1, 0, -1):
            row[i] = row[i] + row[i - 1]
        row.append(1)

        # Imprime la fila
        print("\t".join(str(x) for x in row))
