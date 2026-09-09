#!/usr/bin/env python3
"""Check the tab-separated output produced by exhaustive.cpp."""

import csv
import sys

L = 24_453_922_692
M = 2_375_569_094_238

EXPECTED_INDICES = {
    18: list(range(48, 57)),
    19: list(range(51, 60)),
    20: list(range(54, 63)),
    21: list(range(57, 65)),
}


def main() -> None:
    if len(sys.argv) != 3 or sys.argv[2] not in {"gap", "endpoints", "full-k21"}:
        raise SystemExit("usage: check_results.py FILE {gap|endpoints|full-k21}")
    with open(sys.argv[1], newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    if not rows:
        raise SystemExit("FAIL: no result rows")

    candidates = sorted({
        int(value)
        for row in rows
        for value in row["candidates"].split(",")
        if value
    })
    mode = sys.argv[2]
    if mode == "gap":
        by_k = {}
        for row in rows:
            by_k.setdefault(int(row["k"]), []).append(int(row["m"]))
        assert by_k == EXPECTED_INDICES, (by_k, EXPECTED_INDICES)
        assert candidates == [], candidates
    elif mode == "endpoints":
        assert candidates == [L, M], candidates
    else:
        assert [int(row["m"]) for row in rows] == list(range(57, 66))
        assert candidates == [M], candidates

    print(f"PASS: {mode}; {len(rows)} equations; candidates={candidates}")


if __name__ == "__main__":
    main()
