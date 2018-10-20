#!/usr/bin/env python3
# Type Python_08.fasta as an input
# Split gene sequences into codons

import re

fasta = input('Enter the name of the file ')
FASTA = open(fasta, 'r')

seqs = {}
seq = ''
previous_id = re.search(r'(^>\S*)\s*(.*)', FASTA.readline()).group(1)

for line in FASTA:
  line = line.rstrip()
  match = re.search(r'(^>\S*)\s*(.*)', line)
  if match:
    gene_id = match.group(1)
    if len(seq) > 0:
      seqs[previous_id] = re.findall(r'\w{1,3}', seq)
      seq = ''
      previous_id = gene_id
  else:
    seq = seq + line

seqs[previous_id] = re.findall(r'\w{1,3}', seq)
FASTA.close()

for key in seqs:
  print(key)
  print(' '.join(seqs[key]))







