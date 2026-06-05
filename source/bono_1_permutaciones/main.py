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

    # Procedimiento
    if n == 0 or n == 1:
        procedure = "1"
    elif n <= 10:
        procedure = " * ".join(str(i) for i in range(n, 0, -1))
    else:
        procedure = f"{n} * {n-1} * ... * 1"

    u.print_margin(f"Procedimiento: {n}! = {procedure} = {result}")
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
    
    # Procedimiento recursivo
    if n == 0 or n == 1:
        procedure = "1"
    elif n <= 10:
        procedure = " * ".join(str(i) for i in range(n, 0, -1))
    else:
        procedure = f"{n} * {n-1} * ... * 1"

    u.print_margin(f"Procedimiento (Recursivo): {n}! = {n} * ({n-1})! = ... = {procedure} = {result1}")
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
    k = u.get_integer(f"| Ingrese el valor de k (para permutación, 0 <= k <= {n})", 0, n)
    if k is None:
        return
    result = f.k_permutation(n, k)

    # Procedimiento k-permutación
    if k == 0:
        procedure = "1"
    elif k <= 10:
        procedure = " * ".join(str(i) for i in range(n, n - k, -1))
    else:
        procedure = f"{n} * {n-1} * ... * {n-k+1}"

    u.print_margin(f"Procedimiento: P({n}, {k}) = {n}! / ({n} - {k})! = {procedure} = {result}")
    u.print_margin(
        f"Puedes elegir y ordenar {k} elementos de un conjunto de {n} de {result} formas diferentes"
    )
    u.blank_line()


def compare_two_cases():
    """Compara dos casos de k-permutaciones elegidos por el usuario o por defecto"""
    u.print_margin("Has elegido: Comparar dos casos de k-permutaciones")
    u.print_margin("Ejemplo por defecto: 10 P 3 vs 20 P 5")
    
    use_default = input("| ¿Desea usar el ejemplo por defecto? (S/n): ").strip().lower() != 'n'
    if use_default:
        n1, k1 = 10, 3
        n2, k2 = 20, 5
    else:
        u.print_margin("Primer caso:")
        n1 = u.get_integer("| Ingrese el valor de n1 (entero no negativo)", 0)
        if n1 is None: return
        k1 = u.get_integer(f"| Ingrese el valor de k1 (0 <= k1 <= {n1})", 0, n1)
        if k1 is None: return
        
        u.blank_line()
        u.print_margin("Segundo caso:")
        n2 = u.get_integer("| Ingrese el valor de n2 (entero no negativo)", 0)
        if n2 is None: return
        k2 = u.get_integer(f"| Ingrese el valor de k2 (0 <= k2 <= {n2})", 0, n2)
        if k2 is None: return

    res1 = f.k_permutation(n1, k1)
    res2 = f.k_permutation(n2, k2)
    
    u.blank_line()
    u.print_margin(f"Caso 1: P({n1}, {k1}) = {res1}")
    u.print_margin(f"Caso 2: P({n2}, {k2}) = {res2}")
    u.blank_line()
    
    if res1 > res2:
        diff = res1 - res2
        ratio = res1 / res2 if res2 != 0 else float('inf')
        u.print_margin(f"El Caso 1 tiene {diff} formas más que el Caso 2 (aproximadamente {ratio:.2f} veces más).")
    elif res2 > res1:
        diff = res2 - res1
        ratio = res2 / res1 if res1 != 0 else float('inf')
        u.print_margin(f"El Caso 2 tiene {diff} formas más que el Caso 1 (aproximadamente {ratio:.2f} veces más).")
    else:
        u.print_margin("Ambos casos tienen el mismo número de formas.")
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
    print("| 4. Comparar dos casos de k-permutaciones               |")
    print("| 5. Salir                                               |")
    print("+--------------------------------------------------------+")


# endregion


# Le pide elegir al usuario una opción hasta que decida salir
while True:
    print_header()

    # Bucle principal
    try:
        value = u.get_integer("| Ingrese su opción", 1, 5)
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
                compare_two_cases()
            case 5:
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
