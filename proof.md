# Why the terms are minimal

The current published last term of A188196 is:

```text
L = 24453922692
```

The search covers the single uninterrupted interval:

```text
L + 1 through 4^28 - 1
```

For each base 4 digit length, `exhaustive.cpp` generates every recurrence position that can possibly hit this interval. The lower and upper bounds use the smallest and largest legal digit assignments. Monotonic recurrence coefficients prove that no earlier or later position can work.

At each possible position, the Keith condition is an exact linear equation in the digits. The program enumerates every base 4 digit assignment by splitting the equation into two halves. It keeps duplicate partial sums and reconstructs every matching number. Each match is checked again by direct Keith recurrence simulation.

The complete search output contains exactly the values in `terms.tsv`, in increasing order. Therefore:

- every listed value is a base 4 Keith number;
- no base 4 Keith number was skipped between `L` and any listed value;
- the values are exactly `a(34)` through `a(43)`;
- `a(44)` is greater than `4^28 - 1`, but is not determined here.

The candidate memberships were also checked with Python arbitrary-precision integers and the public `IsKeith[n,b]` function on OEIS. The exhaustive blocks were compiled independently with GCC and Clang, with identical mathematical results. A separate branch-and-bound implementation also reproduced the complete 22-digit block.
