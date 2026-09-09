#!/usr/bin/env python3
"""Standalone checker for the proposed A188196 a(34) certificate."""

N = 2_375_569_094_238
DIGITS = [2, 0, 2, 2, 1, 0, 1, 2, 2, 3, 3, 0, 3, 2, 3, 1, 2, 1, 1, 3, 2]
TERMS = DIGITS + [
    36, 70, 140, 278, 554, 1107, 2214, 4427, 8852, 17702,
    35401, 70799, 141598, 283193, 566384, 1132765, 2265529,
    4531056, 9062111, 18124221, 36248439, 72496876, 144993716,
    289987362, 579974584, 1159948890, 2319897226, 4639793345,
    9279584476, 18559164525, 37118320198, 74236622694,
    148473209987, 296946349175, 593892556752, 1187784830311,
    2375569094238,
]

value = 0
for digit in DIGITS:
    assert 0 <= digit < 4
    value = 4 * value + digit
assert DIGITS[0] != 0
assert value == N

k = len(DIGITS)
assert k == 21
assert len(TERMS) == 58
for i in range(k, len(TERMS)):
    assert TERMS[i] == sum(TERMS[i-k:i]), (i + 1, TERMS[i], sum(TERMS[i-k:i]))
assert TERMS[-1] == N

print("PASS")
print(f"{N} = {''.join(map(str, DIGITS))}_4")
print(f"Keith recurrence hit: a_{len(TERMS)} = {TERMS[-1]}")
