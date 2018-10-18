#!/usr/bin/env python3

IN = open('Python_06.txt', 'r')
OUT = open('Python_06.uc.txt', 'w')
for line in IN:
 line = line.upper()
 OUT.write(line)
IN.close()
OUT.close()









