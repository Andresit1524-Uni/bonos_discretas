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
        + f"| - {result1} formas diferentes (calculado con iteración)\n"
        + f"| - {result2} formas diferentes (calculado con recursión)\n"
        + f"| - {result3} formas diferentes (calculado con memoización)"
    )
    u.blank_line()

    # Verificación de identidad
    u.print_margin(f"Verificación de la identidad de Pascal: C({n}, {k}) = C({n}, {n - k})")
    alt_val = f.iterative_combination(n, n - k)
    u.print_margin(f"- C({n}, {k}) = {result1}")
    u.print_margin(f"- C({n}, {n - k}) = {alt_val}")
    if result1 == alt_val:
        u.print_margin("✓ La identidad se cumple para este caso.")
    else:
        u.print_margin("✗ La identidad no se cumple.")
    u.blank_line()


def make_pascal_row():
    """Pide al usuario un número e imprime la fila n del triángulo de Pascal"""

    u.print_margin("Has elegido: Mostrar fila n del triángulo de Pascal")
    n = u.get_integer("| Ingrese el valor de n (entero no negativo)", 0)
    if n is None:
        return

    row = f.pascal_row(n)
    u.print_margin(f"Fila {n} del triángulo de Pascal:")
    u.print_margin(", ".join(str(x) for x in row))
    u.blank_line()


def make_pascal_triangle():
    """Pide al usuario un número e imprime el triángulo completo"""

    u.print_margin("Has elegido: Mostrar triángulo de Pascal completo")
    n = u.get_integer("| Ingrese el valor de n (entero no negativo)", 0)
    if n is None:
        return

    u.print_margin(f"Triángulo de Pascal hasta {n} filas:")
    f.pascal_triangle(n)
    u.blank_line()


def run_combination_example(title: str, description: str, n: int, k: int):
    """Muestra proceduralmente los pasos de cálculo de un ejemplo de combinación"""
    u.print_margin(f"Ejemplo: {title}")
    u.print_margin(description)
    
    # Cálculo procedural del resultado
    result = f.iterative_combination(n, k)
    
    # Construcción procedural del procedimiento con la fórmula simplificada C(n, k) = C(n, min(k, n-k))
    k_opt = min(k, n - k)
    if k_opt == 0:
        num_str = "1"
        den_str = "1"
    elif k_opt <= 6:
        num_str = " * ".join(str(i) for i in range(n, n - k_opt, -1))
        den_str = " * ".join(str(i) for i in range(k_opt, 0, -1))
    else:
        num_str = f"{n} * {n-1} * ... * {n - k_opt + 1}"
        den_str = f"{k_opt} * {k_opt-1} * ... * 1"
        
    u.print_margin(f"Fórmula: C({n}, {k}) = {n}! / ({k}! * {n - k}!)")
    u.print_margin(f"Aplicando simetría (k_opt = min({k}, {n - k}) = {k_opt}):")
    u.print_margin(f"C({n}, {k_opt}) = ({num_str}) / ({den_str})")
    u.print_margin(f"Resultado = {result} formas.")
    u.blank_line()


def print_examples():
    """Imprime ejemplos prácticos de combinaciones de forma procedural"""

    u.print_margin("Ejemplos prácticos de uso de combinaciones:")
    u.blank_line()
    
    run_combination_example(
        "Elegir un comité",
        "¿De cuántas formas se puede elegir un comité de 3 personas de un grupo de 10?",
        10,
        3
    )
    
    run_combination_example(
        "Manos de póker",
        "¿De cuántas formas se puede recibir una mano de 5 cartas de una baraja estándar de 52?",
        52,
        5
    )
    
    run_combination_example(
        "Lotería",
        "Si en una lotería debes elegir 6 números de entre 49 posibles, ¿cuántos boletos diferentes hay?",
        49,
        6
    )


# endregion


# region Auxiliares


def print_header():
    """Imprime el encabezado de la calculadora"""

    print("+--------------------------------------------------------+")
    print("|              Calculadora de combinaciones              |")
    print("+--------------------------------------------------------+")
    print("| Elige una opción                                       |")
    print("| 1. Calcular combinaciones                              |")
    print("| 2. Imprimir fila n del triángulo de Pascal             |")
    print("| 3. Imprimir triángulo de Pascal completo               |")
    print("| 4. Ver ejemplos de uso                                 |")
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
                make_combination()
            case 2:
                make_pascal_row()
            case 3:
                make_pascal_triangle()
            case 4:
                print_examples()
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
