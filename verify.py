#!/usr/bin/env python3
"""Directly verify every candidate in terms.tsv."""

import csv
from pathlib import Path


def base4(n: int) -> str:
    out = ""
    while n:
        out = str(n % 4) + out
        n //= 4
    return out or "0"


def hit_index(n: int) -> int | None:
    digits = [int(c) for c in base4(n)]
    k = len(digits)
    terms = digits[:]
    while terms[-1] < n:
        terms.append(sum(terms[-k:]))
    return len(terms) if terms[-1] == n else None


rows = list(csv.DictReader(Path(__file__).with_name("terms.tsv").open(encoding="utf-8"), delimiter="\t"))
assert rows

previous = 24_453_922_692
for row in rows:
    n = int(row["decimal"])
    assert n > previous
    assert base4(n) == row["base4"]
    assert len(row["base4"]) == int(row["digits"])
    assert hit_index(n) == int(row["hit_index"])
    previous = n

print(f"PASS: {len(rows)} base-4 Keith numbers")
