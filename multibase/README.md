# Other bases

`../multibase.cpp` is the same solver with the base as its first argument.

```bash
g++ -O3 -std=c++17 -pthread ../multibase.cpp -o multibase
./multibase 3 3 3433683820292512484657849089280 4 > b3.tsv
```

## What was searched

| base | OEIS | published | searched through | found | new |
|---:|---|---:|---|---:|---:|
| 3 | A188195 | 46 | 3^64 - 1 | 107 | +61 |
| 4 | A188196 | 33 | 4^39 - 1 | 67 | +34 |
| 5 | A187713 | 42 | 5^30 - 1 | 92 | +50 |
| 6 | A188197 | 58 | 6^24 - 1 | 83 | +25 |
| 7 | A188198 | 53 | 7^22 - 1 | 77 | +24 |
| 8 | A188199 | 55 | 8^20 - 1 | 70 | +15 |
| 9 | A188200 | 68 | 9^18 - 1 | 82 | +14 |

Every published term was reproduced from scratch first.

Base 10 was a control, not an extension. A007629 is already known to 45 digits by
lattice reduction, which beats this method above base 4. Our run to 10^17 returned
exactly the 63 known terms in that range.

## Filters

Optional, and all must give the same terms. That agreement is part of the
checking.

| flag | what it does | worth |
|---|---|---|
| `--parity` | parity theorem | 2x in odd bases, nothing in even ones |
| `--mod` | residues mod 64 the rest of the digits can reach | 2.2x to 8.6x |
| `--mod2` | adds a second modulus, 63 | 3.2x to 18.9x |

Best is `--parity-first --mod2`. On base 4 through `4^34-1` it cuts the search
from 10.7 to 2.7 billion nodes. It is a constant factor and does not change how
the cost grows.

## Files

- `terms-b<base>.tsv` -- every term, with digit length and hit index
- `bfiles/` -- OEIS-format b-files, ASCII with LF endings
- `submissions/` -- what to paste into each OEIS entry
- `minimality.py` -- rebuilds every equation list without using the solver,
  checks the digit-length blocks tile the range with no gap, re-runs the
  recurrence on every term
- `analyze.py` -- the tables
- `submitpack.py` -- regenerates `submissions/`

## Certificate

```
base  kmax  equations  terms
  3    64      523      107
  4    39      343       67
  5    30      262       92
  6    24      214       83
  7    22      204       77
  8    20      198       70
  9    18      177       82
 10    17      169       63
```

2090 equations, all passing. Run `python minimality.py`. It needs the per-width
block files, which are not committed; regenerate them with the solver first.
