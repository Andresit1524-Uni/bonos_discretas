"""
Utilidades para los bonos, más específicamente para el manejo de interfaz de consola.
"""

from typing import Optional


def get_integer(
    msg: str = "| Ingrese un número: ", min: int = None, max: int = None
) -> Optional[int]:
    """Recibe un número del usuario con validaciones y extremos opcionales"""

    value: int
    first_attempt: bool = True

    while True:
        # Intenta pasar a entero
        try:
            i = input(f"{f'{msg}: ' if first_attempt else '| Intenta de nuevo: '}")

            # Entrada cancelada
            if not i:
                print_margin("Entrada cancelada")
                return None

            value = int(i)

            # Valida los extremos si los tiene
            if min is not None and value < min:
                raise ValueError
            if max is not None and value > max:
                raise ValueError

            break
        except ValueError:
            print_margin("[Error] Entrada no válida")
            first_attempt = False

    return value


def blank_line():
    """Imprime una línea en blanco con margen"""
    print("| ")


def print_margin(text: str):
    """Imprime con un margen"""
    print(f"| {text}")
