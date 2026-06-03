<div align="center">

# Bonos programables - Matemáticas discretas
de **Hayran Andrés López**

</div>

Este repo contiene mi trabajo de bonos programables sobre problemas de conteo de la materia de matemáticas discretas para el 2026-1. Los ejercicios están hechos en Python y documentados en Typst, luego compilados en PDF. Los encuentras en la carpeta [de documentación](./docs/)

Elegí los siguientes dos problemas a resolver:

## Calculadora general de permutaciones y k-permutaciones
La calculadora de permutaciones puede recibir dos enteros $n$ y $k$ y dependiendo del caso elegido por el usuario, calcula la permutación o la k-permutación. Las fórmulas para ambas son, respectivamente:

$$
\begin{aligned}
    P(n) &= n! \\
    P(n,\ k) &= \dfrac{n!}{(n-k)!}
\end{aligned}
$$

El programa valida los valores y tipos ingresados, usa diferentes técnicas como recursión e iteración e imprime los resultados de forma ordenada. Una mejor explicación se encuentra en la [documentación del bono](./docs/bono_1_permutaciones.pdf)

## Calculadora general de combinaciones
La calculadora de combinaciones puede recibir dos enteros $n$ y $k$ y dependiendo del caso elegido por el usuario, calcula la combinación. La fórmula para ello es:

$$
C(n,k) = \dfrac{n!}{k!(n-k)!}
$$

El programa valida los valores y tipos integrados, usa optimizaciones como iteración e:

1. Imprime la fila $n$ del triángulo de Pascal
2. Verifica la identidad de Pascal:

$$
\binom{n}{k} = \binom{n}{n - k}
$$

3. Imprime ejemplos de uso

Al igual que el primer bono, este trabajo valida los datos, incluye diferentes técnicas de programación y las compara. Encuentra más información en la [documentación](./docs/bono_2_combinaciones.pdf)



## Dependencias y uso
Para el correcto uso de este repositorio se necesitan las siguientes herramientas:

1. Python (uso el 3.15 pero debería funcionar cualquiera moderno)
2. [Typst](https://typst.app/open-source/#download) (opcional, si quieres compilar la documentación)
3. Un editor de código (recomendado) y sus extensiones si es el caso.

## Instrucciones
1. Clona este repositorio

    ```bash
    git clone https://github.com/Andresit1524/bonos_discretas
    cd bonos_discretas
    ```

2. Si quieres ejecutar el programa principal:

    ```bash
    py bono_1_permutaciones/main.py
    py bono_2_combinaciones/main.py # Cuando esté listo
    ```

3. Si quieres ejecutar los test

    ```bash
    py bono_1_permutaciones/test.py
    py bono_2_combinaciones/test.py # Cuando esté listo
    ```

4. Si quieres compilar la documentación (aunque ya lo está, es opcional):
   
   > [!Warning]
   > Instala Typst primero y asegúrate que el comando `typst` funcione.

    ```bash
    typst compile docs/source/archivo.typ <docs/archivo.pdf> # Compila una vez
    typst watch docs/source/archivo.typ <docs/archivo.pdf> # Compila en cada guardado si mantienes la terminal
    ```

    Si omites la segunda ruta, Typst elige compilar un PDF al lado del archivo fuente. ¡Cuidado con eso!

## API disponible
Con un script nuevo de Python puedes importar y aprovechar las funciones por tu cuenta.

### Primer bono: permutaciones
Importa el archivo con las funciones así:

```python
# Esto es si el script está en la raíz del proyecto
# Usa autocompletado para que te ayude con la ruta exacta
import bono_1_permutaciones.functions as f
```

Las funciones disponibles son:

```python
# Calcula el factorial con un bucle for
f.iterative_factorial(n: int)

# Calcula el factorial recursivamente
f.recursive_factorial(n: int)

# Calcula el factorial recursivamente usando Tail Call Optimization (TCO)
f.recursive_factorial_tco(n: int)

# Calcula la k-permutación
f.k_permutation(n: int, k: int)
```

La permutación se logra con el factorial como lo vemos en la fórmula del principio.

Conoce la implementación de cada función haciendo `Ctrl + Click` (en el script real en VSCode) o visita [el script directamente](./bono_1_permutaciones/functions.py).

### Segundo bono: combinaciones
_Este esta pendiente de programarse a nivel de API. Espera un poco 🗣️🔥_
