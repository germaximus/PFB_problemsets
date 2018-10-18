#!/usr/bin/env python3

IN = open('Python_06.seq.txt', 'r')
for line in IN:
  line = line.rstrip()
  name, seq = line.split()
  seq = seq[::-1]
  rev_comp = seq.replace('A','a').replace('T','A').replace('a','T').replace('G','g').replace('C','G').replace('g','C')
  print(name +'_reverse_complement' + '\t' + rev_comp) 
IN.close() 






