#import "style.typ": callout, style
#import "utils.typ": pascal_triangle
#show: style.with(header: "Bono 2 - Combinaciones")


= Bono 2 - Combinaciones

#callout()[
  Diseñe un programa que reciba $n$ y $r$, con $0 <= r <= n$, y calcule el número de formas de escoger $r$ objetos entre $n$ objetos distintos sin importar el orden:

  $
    binom(n, r) = n!/(r! (n - r)!)
  $

  El programa debe permitir:

  + Calcular $binom(n, r)$ para cualquier entrada válida
  + Verificar automáticamente la identidad $binom(n, r) = binom(n, n - r)$
  + Generar la fila $n$ del triángulo de Pascal
  + Imprimir ejemplos de uso

  *Extensión opcional:* generar todo el triángulo de Pascal hasta la fila n.
]

== Descripción matemática

=== Combinaciones
Las combinaciones son una técnica de conteo para averiguar todas las formas en las que se puede seleccionar $k$ elementos de un conjunto de $n$ elementos. La fórmula para lograr esto es:

$
  n"C"k = n!/(k! (n - k)!)
$

#quote(block: true)[
  Nótese que es igual a la fórmula de la k-permutación, pero con un $k!$ en el denominador. Esto equivale a tomar todas las combinaciones y dividirlo por las $k!$ posibles órdenes de la selección, para contar solo las selecciones únicas. En otras palabras:

  $
    n"C"k = P(n, k) / k!
  $
]

Es necesario que $k <= n$, porque si no, $n - k$ es negativo, y por ende $(n - k)!$ no existe.

En la combinación el orden de selección de los elementos nunca importa. La permutación puede considerarse un superset de las combinaciones donde el orden si importa.

Otra notación para las combinaciones es la llamada *notación binomial*:

$
  n"C"k = binom(n, k)
$

Esta notación también muy común está asociada con el *teorema de Newton* o teorema del binomio, que usa estos coeficientes para determinar los coeficientes de la potencia de un binomio. No por nada se llaman *coeficientes binomiales*.

=== Triángulo de Pascal
El triángulo de Pascal es una estructura matemática para ordenar los valores de los coeficientes de un triángulo de números. Cada número es la suma de los dos números directamente encima de él. La fila $n$ del triángulo de Pascal corresponde a los coeficientes binomiales $binom(n, k)$ para $k = 0, 1, ..., n$.

#columns(2)[
  #figure(caption: "Triángulo de Pascal hasta el nivel 8")[
    #pascal_triangle(8, hspace: 24pt)
  ]
  #colbreak()
  #figure(caption: "Triángulo de Pascal, en formato de coeficiente binomial")[
    #pascal_triangle(8, hspace: 24pt, binomial: true)
  ]
]

De aquí podemos derivar algunas propiedades:

+ Como el triángulo es simétrico, los lados a la misma distancia de los extremos son iguales en valor. Esto es la *identidad de Pascal*:

  $
    binom(n, k) = binom(n, n - k)
  $

+ Los extremos de las filas son 1, entonces:

  $
    binom(n, 0) = binom(n, n) = 1
  $

+ Sumar dos elementos consecutivos en una fila obtiene el elemento de debajo. Esta es la *regla de Pascal*:

  $
    binom(n, k) + binom(n, k + 1) = binom(n + 1, k + 1)
  $

#pagebreak()

== Implementación

=== Combinaciones recursivas
De forma sencilla, sabemos que tenemos a la mano la librería `math`, la cual ofrece el método `math.comb`:

```py
import math as m

print(m.comb(5, 3)) # -> 10
```

Antes de proceder con el código de nuestra versión, por supuesto, vamos a averiguar como funcionan las combinaciones para desarrollar optimizaciones.

Usando la regla de Pascal sabemos que:

$
  binom(n, k) + binom(n, k - 1) = binom(n + 1, k + 1)
$

Usando esto podemos derivar una forma recursiva de la combinación. La puedes verificar visualmente usando el triángulo de Pascal:

$
  binom(n, k) = binom(n - 1, k) + binom(n - 1, k - 1)
$

Por supuesto, si es recursivo, necesitamos un caso base. Los casos base son:

$
  binom(n, 0) = 1, quad binom(n, n) = 1
$

Implementado en Python nos queda así. Usamos anotaciones de tipo para mejor legibilidad:

```py
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
```

Sin embargo nos pueden preocupar los casos grandes, porque esta función es recursiva y se presta para altos consumos de memoria, calculos duplicados y un riesgo de `RecursionError` en Python.

=== Usando memoización
Para solucionar los problemas de la recursión, podemos usar la *memoización* para guardar los resultados de las combinaciones ya calculadas y evitar cálculos repetidos:

```py
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

    # Recursión
    result = memoized_combination(n - 1, k) + memoized_combination(n - 1, k - 1)
    cached[(n, k)] = result
    return result
```

Esto reducirá los cálculos enormemente, pero igual el consumo de memoria empeora. Sin embargo a la hora de reutilizar ahorra muchísimo tiempo, especialmente para casos grandes donde se generan lotes de resultados precalculados y listos para la próxima.

=== Combinaciones iterativas
Para una última versión de la combinatoria, volvamos a la fórmula original:

$
  binom(n, k) = n!/(k! (n - k)!)
$

Desenrrollando el factorial $n!$ hasta llegar a $(n - k)!$ desarrollamos:

$
  binom(n, k) & = n! / (k! (n - k)!) \
  binom(n, k) & = (n(n - 1)(n - 2) dot ... dot (n - k + 1) cancel((n - k)!)) / (k! cancel((n - k)!)) \
  binom(n, k) & = (n(n - 1)(n - 2) dot ... dot (n - k + 1)) / (k!)
$

Y ahora podemos emparejar cada término del factorial $k!$ con cada término del numerador para obtener dos secuencias:

$
  binom(n, k) & = n/k dot (n - 1)/(k - 1) dot (n - 2)/(k - 2) dot ... dot (n - k + 1)/1 \
  binom(n, k) & = n/1 dot (n - 1)/2 dot (n - 2)/3 dot ... dot (n - k + 1)/k \
$

Podemos generalizarlo con un producto para cada secuencia respectivamente:

$
  binom(n, k) = product_(i = 0)^(k - 1) (n - i)/(k - i) = product_(i = 1)^(k) (n - i + 1)/i
$

Esta es la forma más eficiente de calcular la combinación, al reducirlo a un producto. Sin riesgo de `RecursionError` y con un consumo de memoria constante. Usaremos la segunda versión porque es más adecuada para cálculo basado en enteros:

```py
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
```

Nótese que incluimos una optimización:

```py
# Optimizamos usando la identidad de Pascal
k = min(k, n - k)
```

Como lo dice el comentario, es una aplicación de la *identidad de Pascal*:

$
  binom(n, k) = binom(n, n - k)
$

Esto nos permite reducir el número de términos a calcular, usando el número más pequeño de los dos disponibles sin alterar el resultado. Si funciona, está implementación es la prueba.

#pagebreak()

=== Triángulo de Pascal
Mientras me encontraba escribiendo este artículo para el bono, encontré en internet esta función en Typst para generar los triángulos de Pascal de más arriba:

#link("https://forum.typst.app/t/generating-pascals-triangle/3702")[Fuente]

```typ
#let pascal_triangle(n) = {
  set align(center)
  let row = ()
  for r in range(0, n) {
    // step the row
    for i in range(row.len() - 1, 0, step: -1) {
      row.at(i) = row.at(i) + row.at(i - 1)
    }
    row.push(1)
    // print the row
    grid(
      columns: row.len() * (32pt,),
      align: center,
      //stroke : 0.2pt,
      ..row.map(str)
    )
  }
}
```

Por lo que decidiré reutilizarla en Python para hacer el triángulo en consola. Su funcionamiento se basa en la propiedad:

$
  binom(n + 1, k + 1) = binom(n, k) + binom(n, k + 1)
$

Con la cual sobrescribe una fila para armar la siguiente, elemento por elemento, luego le añade un uno al final para completarle, imprime y repite el proceso. De esta forma, cada fila se construye a partir de la anterior, y se imprime a medida que se va construyendo:

```py
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
```

Además, implementamos una función para obtener únicamente la fila $n$ del triángulo de Pascal (siendo $n$ 0-indexada):

```py
def pascal_row(n: int) -> list[int]:
    """Calcula y devuelve la fila n del triángulo de Pascal (0-indexada)"""

    if type(n) is not int:
        raise TypeError(f"Valor no válido: {n}")
    if n < 0:
        raise ValueError(f"Valor no válido: {n}")

    row = []
    for _ in range(n + 1):
        for i in range(len(row) - 1, 0, -1):
            row[i] = row[i] + row[i - 1]
        row.append(1)

    return row
```

#pagebreak()

=== Aplicación de consola
Para una aplicación de consola solo usaremos `print`s e `input`s para seguir un flujo de usuario básico. También se incluyen verificaciones de errores bien manejados y un código limpio y modular.

El programa estará en el archivo `bono_2_combinaciones/main.py`. Para cumplir estrictamente con los objetivos propuestos, la aplicación permite:

- Calcular combinaciones con verificación automática en tiempo de ejecución de la identidad de Pascal $binom(n, r) = binom(n, n - r)$.
- Generar e imprimir únicamente la fila $n$ del triángulo de Pascal de manera independiente.
- Generar el triángulo completo hasta la fila $n$.
- Visualizar de forma procedural ejemplos cotidianos prácticos (como comités, manos de póker y boletos de lotería) detallando el procedimiento y simplificación de las combinaciones.

=== Pruebas y casos especiales
Para probar este sistema vamos a probar cuatro casos, con varios ejemplos diferentes para cada caso y por cada algoritmo:

+ Números correctos en un rango común (1-100)
+ Uso de negativos y del cero
+ Números grandes (superiores a 1000)
+ Entradas incorrectas (rango o tipo incorrecto)

Este programa estará en el archivo `bono_2_combinaciones/tests.py`

#pagebreak()

== Comentarios y extras
+ Lee los comentarios del primer bono.
+ Al igual que con las permutaciones, la versión iterativa es probablemente la más adecuada por consumo de memoria, rendimiento y menos desperdicio.
+ Tenía pensado hablar de optimización de llamada de cola acá también pero preferí abordar otras formas de optimización y así no tener tantas variantes a comparar.
+ Me he encontrado con buenos recursos para la escritura de estos dos bonos, como #link("https://github.com/vbasky/sublime-vscode-plus")[esta gramática de lenguaje para Sublime] que me permitío añadir resaltado de código estilo VSCode. También disponible en #link("https://gist.github.com/Andresit1524/d5b765ce28f743121907ce3419cfbe80")[este gist con la versión en `tmTheme`] (el formato que Typst usa para sus temas de sintaxis), también disponible en este repo (`vscode_darkplus.tmTheme`).
+ Cada día me arrepiento menos de no haber usado libretas de Jupyter para estos bonos. Hasta dan ganas de crear una alternativa a Jupyter que sí sirva bien. Quizá aprenda Rust para lograrlo. O simplemente use *Weave.jl*.

== Referencias
- Khan Academy. (s.f.). _Introducción a las combinaciones_ [Video]. https://es.khanacademy.org/math/precalculus/x9e81a4f98389efdf:prob-comb/x9e81a4f98389efdf:combinations/v/introduction-to-combinations
- Khan Academy. (s.f.). _Fórmula de las combinaciones_ [Video]. https://es.khanacademy.org/math/precalculus/x9e81a4f98389efdf:prob-comb/x9e81a4f98389efdf:combinations/v/combination-formula
- Wikipedia. (2024). _Triángulo de Pascal_. https://es.wikipedia.org/wiki/Triángulo_de_Pascal
- Wikipedia. (2024). _Coeficiente binomial_. https://es.wikipedia.org/wiki/Coeficiente_binomial
- Universidad Industrial de Santander. (s.f.). _Análisis combinatorio_. Repositorio Noesis. https://noesis.uis.edu.co/server/api/core/bitstreams/d0c3f853-dc1b-4742-9038-6e6b91650b95/content
