# Next base-4 Keith number

Proposed next term of [OEIS A188196](https://oeis.org/A188196):

```text
2375569094238 = 202210122330323121132 (base 4)
```

It occurs at recurrence term 58. No base-4 Keith number lies between the current last term, `24453922692`, and this value.

## Verify

Membership:

```bash
python verify.py
```

Minimality:

```bash
g++ -O3 -std=c++17 -pthread exhaustive.cpp -o exhaustive
./exhaustive 24453922693 2375569094237 4 > gap.tsv
python check_results.py gap.tsv gap
```

Expected result:

```text
PASS: gap; 35 equations; candidates=[]
```

The public `IsKeith[n,b]` verifier on [OEIS A188196](https://oeis.org/A188196) also returns `True` for `IsKeith[2375569094238,4]`.

See [proof.md](proof.md) for the exhaustive argument. GitHub Actions reruns all checks on Ubuntu.
