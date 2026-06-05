import sys
import os

# Añadimos el directorio raíz (source) al path para que Python
# pueda localizar el paquete 'utils'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import functions as f
import utils.utils as u


# region Casos


def make_combination():
    """Pide al usuario dos números y calcula su combinaciones"""

    u.print_margin("Has elegido: Calcular combinaciones")
    n = u.get_integer("| Ingrese el valor de n (entero no negativo)", 0)
    if n is None:
        return
    k = u.get_integer("| Ingrese el valor de k (para combinación, n >= k)", 0)
    if k is None:
        return

    # Resultados por cada método
    result1 = f.iterative_combination(n, k)
    result2 = f.recursive_combination(n, k)
    result3 = f.memoized_combination(n, k)

    u.print_margin(
        f"Puedes elegir {k} elementos de un conjunto de {n} (sin importar el orden) de:\n"
        + f"- {result1} formas diferentes (calculado con iteración)\n"
        + f"- {result2} formas diferentes (calculado con recursión)\n"
        + f"- {result3} formas diferentes (calculado con memoización)\n"
    )
    u.blank_line()


def make_pascal_triangle():
    """Pide al usuario un número y calcula su combinaciones"""

    u.print_margin("Has elegido: Mostrar triángulo de Pascal")
    n = u.get_integer("| Ingrese el valor de n (entero no negativo)", 0)
    if n is None:
        return

    # Resultados por cada método
    u.print_margin(f"Triángulo de Pascal hasta la fila {n} filas:")
    f.pascal_triangle(n)
    u.blank_line()


# endregion


# region Auxiliares


def print_header():
    """Imprime el encabezado de la calculadora"""

    print("+--------------------------------------------------------+")
    print("|              Calculadora de combinaciones              |")
    print("+--------------------------------------------------------+")
    print("| Elige una opción                                       |")
    print("| 1. Calcular combinaciones                              |")
    print("| 2. Imprimir triángulo de Pascal                        |")
    print("| 3. Salir                                               |")
    print("+--------------------------------------------------------+")


# endregion


# Le pide elegir al usuario una opción hasta que decida salir
while True:
    print_header()

    # Bucle principal
    try:
        value = u.get_integer("| Ingrese su opción", 1, 3)
        u.blank_line()
        if value is None:
            u.print_margin("Saliendo (entrada cancelada)")
            break

        match value:
            case 1:
                make_combination()
            case 2:
                make_pascal_triangle()
            case 3:
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
