# Proof outline

Let

```text
L = 24453922692
M = 2375569094238
```

and write a k-digit base-4 integer as `d_1...d_k`, with `d_1` in `{1,2,3}` and every other digit in `{0,1,2,3}`.

## Membership

The digits of M are

```text
2,0,2,2,1,0,1,2,2,3,3,0,3,2,3,1,2,1,1,3,2.
```

Starting with these 21 values and repeatedly summing the preceding 21 terms gives M at the 58th term. The complete sequence is in `certificate.txt` and is checked by `verify.py`.

## Digit equations

Let `C_i` be the i-th coordinate vector for `1 <= i <= k`, and define

```text
C_m = C_(m-k) + ... + C_(m-1),  m > k.
```

Induction gives `a_m=C_m·d`. Let

```text
P = (4^(k-1), 4^(k-2), ..., 1).
```

Then a hit at index m is equivalent to

```text
(P-C_m)·d = 0.
```

This is exact. No approximation, sampling, or probabilistic test is used.

## Complete index range

All coefficients and digits are nonnegative. At index m:

- the smallest possible recurrence value is `C_(m,1)`, attained by digits `[1,0,...,0]`;
- the largest is `3 sum(C_(m,i))`, attained by the all-3 digits.

An index is too early if the maximum is below the interval. Once the minimum exceeds the interval, that index and every later index are impossible because generated recurrence terms are nondecreasing.

For the open gap `(L,M)`, the complete equation ranges are:

| Digits | Integer interval | Indices checked | First later index excluded |
|---:|---:|---:|---:|
| 18 | 24453922693 to 68719476735 | 48 to 56 | 57 |
| 19 | 68719476736 to 274877906943 | 51 to 59 | 60 |
| 20 | 274877906944 to 1099511627775 | 54 to 62 | 63 |
| 21 | 1099511627776 to 2375569094237 | 57 to 64 | 65 |

These four consecutive intervals contain exactly

```text
M-L-1 = 2351115171545
```

integers.

## Exact search

For each equation, `exhaustive.cpp` splits the digits into two groups, enumerates every legal assignment on both sides, sorts one side by its exact weighted sum, and matches every equal opposite sum. Duplicate partial sums are retained, so collisions cannot remove solutions. Candidate integers are reconstructed exactly and filtered against the inclusive interval.

The gap search returns no candidates. The same program:

- reproduces all 33 published A188196 terms through L;
- returns exactly L and M when the interval is expanded to `[L,M]`;
- finds M as the only Keith number in the complete 21-digit block `[4^20,4^21-1]`.

The implementation uses signed 128-bit integers. The largest proved absolute partial-sum bound in the reviewed gap is below `2.60*10^14`, far below even the signed 64-bit maximum of approximately `9.22*10^18`.
