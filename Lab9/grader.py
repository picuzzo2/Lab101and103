#!/usr/bin/env python3

import Lab09_5 as Lab09_5
import sys

i = 0
text = []
for line in sys.stdin:
    i += 1
    line = line.strip()
    if i == 1:
        code_table = line
    elif line:
        text += [line]


Lab09_5.decode(code_table, '\n'.join(text))
print()
