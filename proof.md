# Why the terms are minimal

The last published term of A188196 is:

```text
L = 24453922692
```

The search covers one uninterrupted interval:

```text
L + 1 through 4^34 - 1
```

For each base 4 digit length, both programs generate every recurrence position
that can reach that interval. The lower bound on a position is the value of the
smallest legal digit assignment, the upper bound is the value of the largest.
A position below the block is skipped and a position above it ends the loop,
because the coefficients of the generated terms never decrease. (The initial
coordinate vectors are not monotone; the argument applies from `m = k + 1` on.)

At each position the Keith condition is one exact linear equation in the digits.
Both programs enumerate every legal digit assignment, and every match is checked
again by running the recurrence directly, so a reported candidate cannot be an
artifact of the equation.

The complete output contains exactly the values in `terms.tsv`, in increasing
order. Therefore:

- every listed value is a base 4 Keith number;
- no base 4 Keith number was skipped between `L` and any listed value;
- the values are exactly `a(34)` through `a(57)`;
- any base 4 Keith number beyond `a(57)` is greater than `4^34 - 1`.

## What was actually run

Membership of every term was checked three ways: by `search.cpp`, by
`verify.py` with Python integers, and by the `IsKeith[n,b]` function published on
the OEIS entry.

Minimality up to `4^28 - 1` was produced independently by both programs here,
which use different engines and share no search code. Recorded output from both
runs is in `results`.

Minimality from `4^28` to `4^34 - 1` comes from `search.cpp`; the meet in the
middle cannot reach those widths. That range was reproduced by a separate
branch-and-bound implementation written by Aabir Fauzan while auditing this
repo, which agreed on every term and on the equation list.

That audit also found the defects fixed here: a stale source hash in
`minimality.json`, checkers that used `assert` and so did nothing under
`python -O`, checkers that accepted corrupted result tables, and a
non-terminating input range in `exhaustive.cpp`.
