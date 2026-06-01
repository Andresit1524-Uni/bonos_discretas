#import "style.typ": callout, style
#show: style.with(header: "Bono 2 - Combinaciones")

= Bono 2 - Combinaciones

#callout(color: rgb("#a5f3fc"))[
  Diseñe un programa que reciba $n$ y $r$, con $0 <= r <= n$, y calcule el número de formas de escoger $r$ objetos entre $n$ objetos distintos sin importar el orden:

  $
    binom(n, k) = n!/(k! (n - k)!)
  $

  El programa debe permitir:

  + Calcular $binom(n, r)$ para cualquier entrada válida
  + Verificar automáticamente la identidad $binom(n, k) = binom(n, n - k)$
  + Generar la fila $n$ del triángulo de Pascal
  + Imprimir ejemplos de uso

  *Extensión opcional:* generar todo el triángulo de Pascal hasta la fila n.
]

== Descripión matemática

=== Combinaciones
Las combinaciones son una técnica de conteo para averiguar todas las formas en las que se puede seleccionar $k$ elementos de un conjunto de $n$ elementos. La fórmula para lograr esto es:

$
  n"C"k = n!/(k! (n - k!))
$

#quote(block: true)[
  Nótese que es igual a la fórmula de la k-permutación, pero con un $k!$ en el denominador. Esto equivale a tomar todas las combinaciones y dividirlo por las $k!$ posibles órdenes de la selección, para contar las selecciones únicas. En otras palabras:

  $
    n"C"k = P(n, k)/k!
  $
]

Es necesario que $k <= n$, porque si no, $n - k$ es negativo, y por ende $(n - k)!$ no existe.

En la combinación el orden de selección de los elementos nunca importa. La permutación puede considerarse un superset de las combinaciones donde le orden si importa.

Otra notación para las comabinaciones la llamada *notación binomial*:

$
  n"C"k = binom(n, k)
$

Esta notación también muy común está asociada con el *teorema de Newton* o teorema del binomio, que usa este combinatorias para determinar los coeficientes de la potencia de un binomio.

=== Triángulo de Pascal
El triángulo de Pascal es una estructura matemática para

#pagebreak()

== Implementación

== Comentarios y extras

== Referencias
- https://es.khanacademy.org/math/precalculus/x9e81a4f98389efdf:prob-comb/x9e81a4f98389efdf:combinations/v/introduction-to-combinations
- https://es.khanacademy.org/math/precalculus/x9e81a4f98389efdf:prob-comb/x9e81a4f98389efdf:combinations/v/combination-formula
