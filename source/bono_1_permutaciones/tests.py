"""
Este archivo contiene los tests para los algoritmos de la permutación y k-permutación. Se prueban 4 casos:

1. Casos válidos
2. Casos con negativos y ceros
3. Casos con números grandes
4. Casos con valores erróneos (por tipo o rango)

Por simplicidad se contrastan todos los resultados con math.factorial y math.perm.
"""

import unittest
import math as m
import functions as f


class TestValidInputs(unittest.TestCase):
    """Casos de prueba para casos correctos
    Se han probado con los mismos números para probar que funcionan bajo diferentes algoritmos.
    """

    def test_iterative_factorial(self):
        self.assertEqual(f.iterative_factorial(1), m.factorial(1))
        self.assertEqual(f.iterative_factorial(3), m.factorial(3))
        self.assertEqual(f.iterative_factorial(10), m.factorial(10))
        self.assertEqual(f.iterative_factorial(20), m.factorial(20))

    def test_recursive_factorial(self):
        self.assertEqual(f.recursive_factorial(1), m.factorial(1))
        self.assertEqual(f.recursive_factorial(3), m.factorial(3))
        self.assertEqual(f.recursive_factorial(10), m.factorial(10))
        self.assertEqual(f.recursive_factorial(20), m.factorial(20))

    def test_recursive_factorial_tco(self):
        self.assertEqual(f.recursive_factorial_tco(1), m.factorial(1))
        self.assertEqual(f.recursive_factorial_tco(3), m.factorial(3))
        self.assertEqual(f.recursive_factorial_tco(10), m.factorial(10))
        self.assertEqual(f.recursive_factorial_tco(20), m.factorial(20))

    def test_k_permutation(self):
        self.assertEqual(f.k_permutation(10, 6), m.perm(10, 6))
        self.assertEqual(f.k_permutation(20, 2), m.perm(20, 2))
        self.assertEqual(f.k_permutation(30, 5), m.perm(30, 5))
        self.assertEqual(f.k_permutation(54, 4), m.perm(54, 4))


class TestNegativesAndZeros(unittest.TestCase):
    """Casos de prueba para números negativos y ceros"""

    def test_iterative_factorial(self):
        # Caso correcto: 0! = (-0)! = 1
        self.assertEqual(f.iterative_factorial(0), 1)
        self.assertEqual(f.iterative_factorial(-0), 1)

        # Negativos siempre fallan
        with self.assertRaises(ValueError):
            f.iterative_factorial(-63)
        with self.assertRaises(ValueError):
            f.iterative_factorial(-75)

    def test_recursive_factorial(self):
        # Caso correcto: 0! = (-0)! = 1
        self.assertEqual(f.recursive_factorial(0), 1)
        self.assertEqual(f.recursive_factorial(-0), 1)

        # Negativos siempre fallan
        with self.assertRaises(ValueError):
            f.recursive_factorial(-63)
        with self.assertRaises(ValueError):
            f.recursive_factorial(-75)

    def test_recursive_factorial_tco(self):
        # Caso correcto: 0! = (-0)! = 1
        self.assertEqual(f.recursive_factorial_tco(0), 1)
        self.assertEqual(f.recursive_factorial_tco(-0), 1)

        # Negativos siempre fallan
        with self.assertRaises(ValueError):
            f.recursive_factorial_tco(-63)
        with self.assertRaises(ValueError):
            f.recursive_factorial_tco(-75)

    def test_k_permutation(self):
        # Permutacines con cero
        self.assertEqual(f.k_permutation(1, 0), 1)
        self.assertEqual(f.k_permutation(0, 0), 1)

        # Negativos siempre fallan
        with self.assertRaises(ValueError):
            self.assertEqual(f.k_permutation(-12, 3))
        with self.assertRaises(ValueError):
            self.assertEqual(f.k_permutation(12, -3))


class TestBigNumbers(unittest.TestCase):
    """Casos de prueba para números grandes (encima de 1001).

    Estos casos fallan si son recursivos por RecursionError. En formas iterativas no hay problema
    excepto por el consumo de tiempo por multiplicaciones, que puede ser muy alto.

    Las k-permutaciones son iterativas, por lo que tampoco sufren de RecursionError.
    """

    # El factorial iterativo funciona bien con números así
    def test_iterative_factorial(self):
        self.assertEqual(f.iterative_factorial(1001), m.perm(1001))
        self.assertEqual(f.iterative_factorial(2000), m.perm(2000))
        self.assertEqual(f.iterative_factorial(4980), m.perm(4980))
        self.assertEqual(f.iterative_factorial(10000), m.perm(10000))

    # La recursión siempre falla por valores mayores a 1000 con RecursionError
    def test_recursive_factorial(self):
        with self.assertRaises(RecursionError):
            f.recursive_factorial(1001)
        with self.assertRaises(RecursionError):
            f.recursive_factorial(2000)
        with self.assertRaises(RecursionError):
            f.recursive_factorial(4980)
        with self.assertRaises(RecursionError):
            f.recursive_factorial(10000)

    # La recursión siempre falla por valores mayores a 1000 con RecursionError
    # TCO manual no nos salva de esto
    def test_recursive_factorial_tco(self):
        with self.assertRaises(RecursionError):
            f.recursive_factorial_tco(1001)
        with self.assertRaises(RecursionError):
            f.recursive_factorial_tco(2000)
        with self.assertRaises(RecursionError):
            f.recursive_factorial_tco(4980)
        with self.assertRaises(RecursionError):
            f.recursive_factorial_tco(10000)

    # La k-permutación funciona bien con números así
    def test_k_permutation(self):
        self.assertEqual(f.k_permutation(1001, 233), m.perm(1001, 233))
        self.assertEqual(f.k_permutation(2000, 433), m.perm(2000, 433))
        self.assertEqual(f.k_permutation(4980, 3), m.perm(4980, 3))
        self.assertEqual(f.k_permutation(10000, 98), m.perm(10000, 98))


class TestWrongInputs(unittest.TestCase):
    """Casos de prueba para entradas no válidas (no incluye errores por números grandes)

    - Para factoriales, los errores solo se dan con números negativos
    - Para permutaciones, también puede pasar si k > n
    - En todo caso, cualquier valor no numérico fallará
    """

    def test_iterative_factorial(self):
        # Negativos
        with self.assertRaises(ValueError):
            f.iterative_factorial(-1)
        with self.assertRaises(ValueError):
            f.iterative_factorial(-24)

        # Tipo incorrecto
        with self.assertRaises(TypeError):
            f.iterative_factorial("85")
        with self.assertRaises(TypeError):
            f.iterative_factorial([])

    def test_recursive_factorial(self):
        # Negativos
        with self.assertRaises(ValueError):
            f.recursive_factorial(-1)
        with self.assertRaises(ValueError):
            f.recursive_factorial(-24)

        # Tipo incorrecto
        with self.assertRaises(TypeError):
            f.recursive_factorial([])
        with self.assertRaises(TypeError):
            f.recursive_factorial(3.4)

    def test_recursive_factorial_tco(self):
        # Negativos
        with self.assertRaises(ValueError):
            f.recursive_factorial_tco(-1)
        with self.assertRaises(ValueError):
            f.recursive_factorial_tco(-24)

        # Tipo incorrecto
        with self.assertRaises(TypeError):
            f.recursive_factorial_tco("-85")
        with self.assertRaises(TypeError):
            f.recursive_factorial_tco(True)

    def test_k_permutation(self):
        # Negativos
        with self.assertRaises(ValueError):
            f.k_permutation(-1, 5)
        with self.assertRaises(ValueError):
            f.k_permutation(45, -23)

        # k > n
        with self.assertRaises(ValueError):
            f.k_permutation(45, 100)
        with self.assertRaises(ValueError):
            f.k_permutation(1, 34)

        # Tipo incorrecto (extras)
        with self.assertRaises(TypeError):
            f.k_permutation(45, "100")
        with self.assertRaises(TypeError):
            f.k_permutation(True, 34)


if __name__ == "__main__":
    unittest.main()
