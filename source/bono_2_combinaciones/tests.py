"""
Este archivo contiene los tests para los algoritmos de combinación y el triángulo de Pascal. Se prueban 4 casos:

1. Casos válidos
2. Casos con negativos y ceros
3. Casos con números grandes
4. Casos con valores erróneos (por tipo o rango)

Por simplicidad se contrastan todos los resultados con math.comb.
"""

import unittest
import math as m
import functions as f


class TestValidInputs(unittest.TestCase):
    """Casos de prueba para casos correctos"""

    def test_recursive_combination(self):
        self.assertEqual(f.recursive_combination(5, 2), m.comb(5, 2))
        self.assertEqual(f.recursive_combination(10, 5), m.comb(10, 5))
        self.assertEqual(f.recursive_combination(15, 0), m.comb(15, 0))
        self.assertEqual(f.recursive_combination(15, 15), m.comb(15, 15))

    def test_memoized_combination(self):
        self.assertEqual(f.memoized_combination(5, 2), m.comb(5, 2))
        self.assertEqual(f.memoized_combination(10, 5), m.comb(10, 5))
        self.assertEqual(f.memoized_combination(15, 0), m.comb(15, 0))
        self.assertEqual(f.memoized_combination(15, 15), m.comb(15, 15))

    def test_iterative_combination(self):
        self.assertEqual(f.iterative_combination(5, 2), m.comb(5, 2))
        self.assertEqual(f.iterative_combination(10, 5), m.comb(10, 5))
        self.assertEqual(f.iterative_combination(15, 0), m.comb(15, 0))
        self.assertEqual(f.iterative_combination(15, 15), m.comb(15, 15))

    def test_pascal_row(self):
        self.assertEqual(f.pascal_row(0), [1])
        self.assertEqual(f.pascal_row(1), [1, 1])
        self.assertEqual(f.pascal_row(4), [1, 4, 6, 4, 1])



class TestNegativesAndZeros(unittest.TestCase):
    """Casos de prueba para números negativos y ceros"""

    def test_recursive_combination(self):
        # Casos correctos con 0
        self.assertEqual(f.recursive_combination(0, 0), 1)
        self.assertEqual(f.recursive_combination(5, 0), 1)

        # Negativos fallan
        with self.assertRaises(ValueError):
            f.recursive_combination(-5, 2)
        with self.assertRaises(ValueError):
            f.recursive_combination(5, -2)

    def test_memoized_combination(self):
        # Casos correctos con 0
        self.assertEqual(f.memoized_combination(0, 0), 1)
        self.assertEqual(f.memoized_combination(5, 0), 1)

        # Negativos fallan
        with self.assertRaises(ValueError):
            f.memoized_combination(-5, 2)
        with self.assertRaises(ValueError):
            f.memoized_combination(5, -2)

    def test_iterative_combination(self):
        # Casos correctos con 0
        self.assertEqual(f.iterative_combination(0, 0), 1)
        self.assertEqual(f.iterative_combination(5, 0), 1)

        # Negativos fallan
        with self.assertRaises(ValueError):
            f.iterative_combination(-5, 2)
        with self.assertRaises(ValueError):
            f.iterative_combination(5, -2)

    def test_pascal_triangle(self):
        # Cero o negativos
        with self.assertRaises(ValueError):
            f.pascal_triangle(-5)

    def test_pascal_row(self):
        # Negativos fallan
        with self.assertRaises(ValueError):
            f.pascal_row(-5)
        with self.assertRaises(ValueError):
            f.pascal_row(-1)



class TestBigNumbers(unittest.TestCase):
    """Casos de prueba para números grandes (encima del límite de recursión)."""

    def test_iterative_combination(self):
        self.assertEqual(f.iterative_combination(1001, 233), m.comb(1001, 233))
        self.assertEqual(f.iterative_combination(2000, 433), m.comb(2000, 433))

    def test_recursive_combination(self):
        with self.assertRaises(RecursionError):
            f.recursive_combination(1001, 233)

    def test_memoized_combination(self):
        # Si no está cacheado, también fallará por recursión si n es muy grande
        # Limpiamos la caché primero para asegurar que se pruebe la recursión profunda
        f.cached.clear()
        with self.assertRaises(RecursionError):
            f.memoized_combination(1001, 233)


class TestWrongInputs(unittest.TestCase):
    """Casos de prueba para entradas no válidas por tipo o rango"""

    def test_recursive_combination(self):
        # k > n
        with self.assertRaises(ValueError):
            f.recursive_combination(5, 10)

        # Tipos incorrectos
        with self.assertRaises(TypeError):
            f.recursive_combination("5", 2)
        with self.assertRaises(TypeError):
            f.recursive_combination(5, [2])

    def test_memoized_combination(self):
        # k > n
        with self.assertRaises(ValueError):
            f.memoized_combination(5, 10)

        # Tipos incorrectos
        with self.assertRaises(TypeError):
            f.memoized_combination("5", 2)
        with self.assertRaises(TypeError):
            f.memoized_combination(5, [2])

    def test_iterative_combination(self):
        # k > n
        with self.assertRaises(ValueError):
            f.iterative_combination(5, 10)

        # Tipos incorrectos
        with self.assertRaises(TypeError):
            f.iterative_combination("5", 2)
        with self.assertRaises(TypeError):
            f.iterative_combination(5, [2])

    def test_pascal_triangle(self):
        # Tipos incorrectos
        with self.assertRaises(TypeError):
            f.pascal_triangle("5")
        with self.assertRaises(TypeError):
            f.pascal_triangle(3.5)

    def test_pascal_row_wrong_type(self):
        # Tipos incorrectos
        with self.assertRaises(TypeError):
            f.pascal_row("5")
        with self.assertRaises(TypeError):
            f.pascal_row(3.5)



if __name__ == "__main__":
    unittest.main()
