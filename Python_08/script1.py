#!/usr/bin/env python3
# Type Python_08.fasta as an input
# Counts ATCG content for every gene record

import re

fasta = input('Enter the name of the file ')
if not fasta.endswith(('.fasta','.fa', '.nt')): raise ValueError('Input is not in a fasta file format')

try:
  FASTA = open(fasta, 'r')
except: print('File', fasta, 'does not exist')

seq = ''
gene_name = ''
gene_descr = ''

for line in FASTA:
  line = line.rstrip()
  match = re.search(r'(^>\S*)(\s*.*)', line)
  if match:
     if len(seq) > 0:
         print(gene_name, seq.count('A'), seq.count('T'), seq.count('G'), seq.count('C'))
         A_count = seq.count('A')
         T_count = seq.count('T')
         G_count = seq.count('G')
         C_count = seq.count('C')
         gene_name = match.group(1).lstrip('>')
         gene_descr = match.group(2)
         seq = ''
  else:
    seq = seq + line
print(gene_name, seq.count('A'), seq.count('T'), seq.count('G'), seq.count('C'))
FASTA.close()




















