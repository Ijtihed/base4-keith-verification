# Base 4 Keith numbers

This repo verifies a proposed continuation of [OEIS A188196](https://oeis.org/A188196).

The published list ends at:

```text
a(33) = 24453922692
```

The exact search found the next ten terms, `a(34)` through `a(43)`. See [terms.tsv](terms.tsv).

## Quick check

```bash
python verify.py
```

This checks directly that every listed value is a base 4 Keith number.

## Full minimality check

```bash
g++ -O3 -std=c++17 -pthread exhaustive.cpp -o exhaustive
./exhaustive 24453922693 72057594037927935 1 > all.tsv
python check_results.py all.tsv all
```

This exhausts every integer after `a(33)` through `4^28 - 1`. It takes about 15 minutes and about 2 GB of memory on the machine used here.

The search found exactly the ten values in [terms.tsv](terms.tsv). Therefore they are consecutive, not merely examples. No claim is made about `a(44)`.

See [method.md](method.md) for the idea and prior work, and [proof.md](proof.md) for the minimality argument.
