#!/usr/bin/env python3

import re

IN = open('Python_07_nobody.txt', 'r')
OUT = open('Alice.txt', 'w')
for line in IN:
  line = line.rstrip()
  new_line = re.sub(r'Nobody',r'Alice', line)
  OUT.write(new_line + '\n')

IN.close()
OUT.close()





