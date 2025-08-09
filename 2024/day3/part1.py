#!/usr/bin/env python

import sys
import re

s = 0
p = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
for line in sys.stdin:
    matches = re.findall(p, line)
    for m in matches:
        s += int(m[0]) * int(m[1])
print(s)
