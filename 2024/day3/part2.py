#!/usr/bin/env python

import sys
import re

s = 0
mul_p = r'mul\(([0-9]{1,3}),([0-9]{1,3})\)'
do_p = r'do\(\)'
dont_p = r'don\'t\(\)'
p = rf'({mul_p}|{do_p}|{dont_p})'
enabled = True
for line in sys.stdin:
    matches = re.findall(p, line)
    for m in matches:
        if re.match(do_p, m[0]):
            enabled = True
        elif re.match(dont_p, m[0]):
            enabled = False
        elif enabled:
            s += int(m[1]) * int(m[2])
print(s)
