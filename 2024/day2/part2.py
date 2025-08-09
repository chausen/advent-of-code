#!/usr/bin/env python3

import sys

# Problematic lines:
# Removed 1 from [54, 56, 54, 52, 51, 49]
# - removing 0 would work though

def isMonotonic(inc, prev, curr):
    return (inc and curr > prev) or (not inc and curr < prev)

def isSafe(report):
    inc = report[0] < report[1]
    for i in range(1, len(report)):
        prev, curr = report[i-1], report[i]
        diff = abs(curr - prev)
        if (not isMonotonic(inc, prev, curr) or
            diff < 1 or diff > 3):
            return False, i
    return True, -1

numSafe = 0
for line in sys.stdin:
    report = list(map(int, line.split()))
    safe, i = isSafe(report)
    if not safe:
        safe = (isSafe(report[:i-1] + report[i+0:])[0] or
                isSafe(report[:i-2] + report[i-1:])[0] or
                isSafe(report[:i+0] + report[i+1:])[0])
        # safe1, _ = isSafe(report[:i-1] + report[i:])
        # safe2, _ = isSafe(report[:i-2] + report[i-1:])
        # safe = safe1 or safe2
        # if safe:
        #     print(f'Removed {i if safe1 else i-1} from {report}')
    if safe:
        numSafe += 1

print(numSafe)
