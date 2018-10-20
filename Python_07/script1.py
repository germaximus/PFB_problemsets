#!/usr/bin/env python3

import re

IN = open('Python_07_nobody.txt', 'r')

for line in IN:
 line = line.rstrip()
 match = re.search(r'Nobody', line)
 if match: print(match.start())


IN.close()



