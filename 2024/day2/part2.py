#!/usr/bin/env python3

import sys

numSafe = 0
for line in sys.stdin:
    report = list(map(int, line.split()))
    inc = report[0] < report[1]
    safe = True
    tolerances = 1
    for i in range(1, len(report)):
        diff = abs(report[i] - report[i-1])
        if ((inc and report[i] < report[i-1]) or
            (not inc and report[i] > report[i-1]) or
            diff < 1 or diff > 3):
            # The whole report has to work if we remove a level
            # that would make it unsafe...we are not checking that
            if tolerances > 0:
                tolerances -= 1
            else:
                safe = False
                break
    if safe:
        numSafe += 1

print(numSafe)
