#!/usr/bin/env python

import sys

left, right = [], []
for line in sys.stdin:
    l, r = tuple(map(int, (line.strip().split('   '))))
    left.append(l)
    right.append(r)

left.sort()
right.sort()
distance = 0
for i in range(0, len(left)):
    distance += abs(left[i] - right[i])

print(distance)
