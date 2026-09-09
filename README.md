# Base 4 Keith numbers

This repo extends [OEIS A188196](https://oeis.org/A188196).

The published list ends at:

```text
a(33) = 24453922692
```

An exact search found the next twenty-four terms, `a(34)` through `a(57)`. The new
ones are in [terms.tsv](terms.tsv); the whole list from `a(1)` is in
[b188196.txt](b188196.txt).

## Quick check

```bash
python verify.py
```

Runs the base 4 Keith recurrence on every listed value and checks the widths,
the hit positions, and the two files against each other.

## Full minimality check

```bash
g++ -O3 -std=c++17 -pthread search.cpp -o search
./search 24453922693 295147905179352825855 12 > all.tsv
python check_results.py all.tsv 24453922693 295147905179352825855
```

This covers every integer after `a(33)` through `4^34 - 1`. It takes about fifteen
seconds on twelve threads and needs almost no memory. The result is exactly the
twenty-four values in `terms.tsv`, so they are consecutive rather than a
selection. Any further term is greater than `4^34 - 1`.

`check_results.py` rebuilds the expected equation list itself and re-derives every
candidate, so it fails if the search skipped a position or mislabelled a row.

## Second implementation

`exhaustive.cpp` solves the same equations by meet in the middle. It agrees with
`search.cpp` on everything up to `4^28 - 1`, which is as far as its sorted table
fits in memory:

```bash
g++ -O3 -std=c++17 -pthread exhaustive.cpp -o exhaustive
./exhaustive 24453922693 72057594037927935 12 > mitm.tsv
python check_results.py mitm.tsv 24453922693 72057594037927935
```

Recorded output from both is in [results](results).

See [method.md](method.md) for the idea and prior work, and [proof.md](proof.md)
for the minimality argument.
