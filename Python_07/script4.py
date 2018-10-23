#!/usr/bin/env python3

import re

IN = open('Python_07_ApoI.fasta', 'r')

#test1 = IN.readline() #read one line (remembers position like <> in Perl)

seq = ''
for line in IN:
  print(line)
  for line in IN:
    line = line.rstrip()
    seq = seq + line

site = re.findall(r'[AG]AATT[CT]', seq)
print(seq)
print(site)


IN.close()










