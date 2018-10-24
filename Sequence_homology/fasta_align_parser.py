#!/usr/bin/env python3

import re

FILE = open('out.txt', 'r')
 

for line in FILE:
   match = re.search(r'>>>.+ Precursor - (\d+) aa', line)
   if match:
     query_length = int(match.group(1))
     print('Query length:', query_length)
     break

hodor = 0
for line in FILE:
      match = re.search(r'^>>(\S*)', line)
      if match: 
        print(match.group(1) + '\t', end = '')
        for line in FILE:
           if(hodor == 1): 
              hodor = 0
              break
           match = re.search(r'bits: (\d+\.\d+)', line)
           if match:          
             print('\t', match.group(1), end = '')
             for line in FILE:
                match = re.search(r'in (\d+) aa overlap', line)
                if match:
                  print('\t', match.group(1), end = '')
                  print('\t', str(round(int(match.group(1))/query_length*100, 1)) + '%')
                  hodor += 1
                  break
             
           



















