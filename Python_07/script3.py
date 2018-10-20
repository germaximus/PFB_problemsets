#!/usr/bin/env python3

import re

IN = open('Python_07.fasta', 'r')
for line in IN:
 match =  re.search(r'(^>\S*)\s+(.*)', line)
 if match: 
  print('Gene id:', match.group(1), 'description:', match.group(2))

IN.close()











