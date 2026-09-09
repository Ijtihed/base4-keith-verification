# Method

Suppose a base 4 number has digits `d1,...,dk`.

Every later term of its Keith recurrence is a linear combination of those digits.
For each possible hit position `m`, the condition that the recurrence term equals
the original number becomes one exact equation:

```text
(base-4 place values - recurrence coefficients) dot digits = 0
```

Only finitely many hit positions need checking. Before the first possible
position, even the largest digit assignment is too small. After the last, even
the smallest leading-digit assignment is too large, and the coefficients of the
generated terms never decrease, so no later position can work either.

Two programs solve those equations.

`exhaustive.cpp` splits the digits into two groups, enumerates every legal
assignment on each side, sorts one side by its weighted sum, and finds equal
opposite sums by binary search. Duplicate sums are kept. The sorted table holds
`4^(k/2)` entries, which is 2 GB at 28 digits and 8 GB at 29, so this is the
practical ceiling.

`search.cpp` avoids the table. Shifting every weight up by the most negative one
makes them all nonnegative, at the cost of turning the right-hand side into
`shift * digitsum`. Fixing the digit sum then makes the reachable interval of any
remaining suffix tight, so branch and bound prunes hard. It needs no table and
reaches 34 digits in seconds.

All arithmetic is exact 128-bit integer arithmetic. Floating point is used only
for timing.

## Prior work

The general idea is not new. Keith-number searches were reduced to bounded linear
Diophantine equations decades ago. Ken Sherriff published an equation-splitting
lookup-table method in 1994. Mike Keith later described improved exhaustive
searches, and Daniel Lichtblau published a lattice and integer-programming
approach in 2006.

This repo contributes the base 4 computation and its reproducible output, not the
invention of equation splitting.

References:

- [Mike Keith, Keith Numbers](https://www.cadaeic.net/keithnum.htm)
- [MathWorld bibliography for Keith numbers](https://mathworld.wolfram.com/KeithNumber.html)
- [Daniel Lichtblau, Making Change and Finding Repfigits: Balancing a Knapsack](https://doi.org/10.1007/11832225_16)
