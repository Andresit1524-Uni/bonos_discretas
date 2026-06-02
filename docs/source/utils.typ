/// Prints a Pascal's triangle of n rows, optionally with binomial coefficients instead of the raw numbers. The spacing between columns can be adjusted with hspace.
///
/// Source: https://forum.typst.app/t/generating-pascals-triangle/3702
#let pascal_triangle(n, binomial: false, hspace: 32pt) = {
  set align(center)
  let row = ()
  for r in range(n) {
    // Arma la fila calculando y sobrescribiendo la anterior
    for i in range(row.len() - 1, 0, step: -1) {
      row.at(i) = row.at(i) + row.at(i - 1)
    }
    row.push(1)

    // Imprime la fila
    grid(
      columns: row.len() * (hspace,),
      align: center,
      // stroke : 0.2pt,
      ..if binomial {
        range(row.len()).map(k => $binom(#str(r), #k)$)
      } else {
        row.map(str)
      }
    )
  }
}
