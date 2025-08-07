#!/usr/bin/env python3

import sys
from collections import defaultdict

left, right = [], []
for line in sys.stdin:
    l, r = tuple(map(int, (line.strip().split('   '))))
    left.append(l)
    right.append(r)

rightCounts = defaultdict(int)
for num in right:
    rightCounts[num] += 1

score = 0
for num in left:
    score += num * rightCounts[num]

print(score)
