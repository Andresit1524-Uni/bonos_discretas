import sys
import os

# Añadimos el directorio raíz (source) al path para que Python
# pueda localizar el paquete 'utils'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import functions as f
import utils.utils as u


# region Casos


def make_iterative_permutation():
    """Pide al usuario un número y calcula su permutación usando factorial iterativo"""

    u.print_margin("Has elegido: Calcular permutaciones (factorial iterativo)")
    n = u.get_integer("| Ingrese el valor de n (entero no negativo)", 0)
    if n is None:
        return
    result: int = f.iterative_factorial(n)

    u.print_margin(f"Puedes permutar {n} elementos de {result} formas diferentes")
    u.print_margin("Calculado de forma iterativa")
    u.blank_line()


def make_recursive_permutation():
    """Pide al usuario un número y calcula su permutación usando factorial recursivo con
    optimización de cola (TCO)
    """

    u.print_margin("Has elegido: Calcular permutaciones (factorial recursivo)")
    n = u.get_integer("| Ingrese el valor de n (entero no negativo)", 0)
    if n is None:
        return

    result1: int = f.recursive_factorial(n)
    u.print_margin(f"Puedes permutar {n} elementos de {result1} formas diferentes")
    u.print_margin("Calculado de forma recursiva")
    u.blank_line()

    result2: int = f.recursive_factorial_tco(n)
    u.print_margin(f"Puedes permutar {n} elementos de {result2} formas diferentes")
    u.print_margin("Calculado de forma recursiva con TCO")
    u.blank_line()


def make_k_permutation():
    """Pide al usuario dos números y calcula su k-permutación"""

    u.print_margin("Has elegido: Calcular k-permutaciones")
    n = u.get_integer("| Ingrese el valor de n (entero no negativo)", 0)
    if n is None:
        return
    k = u.get_integer("| Ingrese el valor de k (para permutación, n >= k)", 0)
    if k is None:
        return
    result = f.k_permutation(n, k)

    u.print_margin(
        f"Puedes elegir {k} elementos de un conjunto de {n} de {result} formas diferentes"
    )
    u.blank_line()


# endregion


# region Auxiliares


def print_header():
    """Imprime el encabezado de la calculadora"""

    print("+--------------------------------------------------------+")
    print("|       Calculadora de factoriales y permutaciones       |")
    print("+--------------------------------------------------------+")
    print("| Elige una opción                                       |")
    print("| 1. Calcular permutaciones (factorial iterativo)        |")
    print("| 2. Calcular permutaciones (factorial recursivo)        |")
    print("| 3. Calcular k-permutaciones                            |")
    print("| 4. Salir                                               |")
    print("+--------------------------------------------------------+")


# endregion


# Le pide elegir al usuario una opción hasta que decida salir
while True:
    print_header()

    # Bucle principal
    try:
        value = u.get_integer("| Ingrese su opción", 1, 4)
        u.blank_line()
        if value is None:
            u.print_margin("Saliendo (entrada cancelada)")
            break

        match value:
            case 1:
                make_iterative_permutation()
            case 2:
                make_recursive_permutation()
            case 3:
                make_k_permutation()
            case 4:
                u.print_margin("Saliendo")
                break
    except ValueError as e:
        os.system("cls" if os.name == "nt" else "clear")
        u.print_margin(
            f"Error: {e}. Por favor, asegúrese de ingresar números enteros válidos."
        )
        u.blank_line()
    except Exception as e:
        os.system("cls" if os.name == "nt" else "clear")
        u.print_margin(f"Ocurrió un error inesperado: {e}")
        u.blank_line()
