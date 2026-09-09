#!/usr/bin/env python3
"""Check tab-separated output produced by exhaustive.cpp."""

import csv
import sys

L = 24_453_922_692
M = 2_375_569_094_238
LIMIT = 4**28 - 1
ALL = [
    2_375_569_094_238,
    5_473_352_509_055,
    9_742_923_197_455,
    152_038_348_048_545,
    353_387_237_261_042,
    1_039_642_015_534_604,
    2_431_494_812_438_214,
    5_217_766_440_390_935,
    47_453_708_818_892_663,
    57_341_012_950_430_378,
]

EXPECTED_GAP_INDICES = {
    18: list(range(48, 57)),
    19: list(range(51, 60)),
    20: list(range(54, 63)),
    21: list(range(57, 65)),
}

EXPECTED_ALL_INDICES = {
    18: list(range(48, 57)),
    19: list(range(51, 60)),
    20: list(range(54, 63)),
    21: list(range(57, 66)),
    22: list(range(60, 69)),
    23: list(range(62, 72)),
    24: list(range(65, 75)),
    25: list(range(68, 78)),
    26: list(range(71, 81)),
    27: list(range(74, 84)),
    28: list(range(77, 87)),
}


def candidates(rows: list[dict[str, str]]) -> list[int]:
    return sorted({
        int(value)
        for row in rows
        for value in row["candidates"].split(",")
        if value
    })


def main() -> None:
    modes = {"gap", "endpoints", "full-k21", "all"}
    if len(sys.argv) != 3 or sys.argv[2] not in modes:
        raise SystemExit("usage: check_results.py FILE {gap|endpoints|full-k21|all}")

    with open(sys.argv[1], newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    assert rows, "no result rows"

    found = candidates(rows)
    mode = sys.argv[2]
    if mode == "gap":
        by_k: dict[int, list[int]] = {}
        for row in rows:
            by_k.setdefault(int(row["k"]), []).append(int(row["m"]))
        assert by_k == EXPECTED_GAP_INDICES
        assert found == []
    elif mode == "endpoints":
        assert found == [L, M]
    elif mode == "full-k21":
        assert [int(row["m"]) for row in rows] == list(range(57, 66))
        assert found == [M]
    else:
        by_k: dict[int, list[dict[str, str]]] = {}
        for row in rows:
            by_k.setdefault(int(row["k"]), []).append(row)
        assert {
            k: [int(row["m"]) for row in block]
            for k, block in by_k.items()
        } == EXPECTED_ALL_INDICES
        for k, block in by_k.items():
            expected_lower = L + 1 if k == 18 else 4 ** (k - 1)
            expected_upper = 4**k - 1
            assert {int(row["lower"]) for row in block} == {expected_lower}
            assert {int(row["upper"]) for row in block} == {expected_upper}
        assert found == ALL

    print(f"PASS: {mode}; {len(rows)} equations; candidates={found}")


if __name__ == "__main__":
    main()
