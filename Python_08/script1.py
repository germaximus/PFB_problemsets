#!/usr/bin/env python3
# Type Python_08.fasta as an input
# Counts ATCG content for every gene record

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
      A_count = seq.count('A')
      T_count = seq.count('T')
      G_count = seq.count('G')
      C_count = seq.count('C')
      seqs[previous_id] = {'A' : A_count, 'T' : T_count, 'G' : G_count, 'C' : C_count}
      seq = ''
      previous_id = gene_id
  else:
    seq = seq + line

seqs[previous_id] = {'A' : seq.count('A'), 'T' : seq.count('T'), 'G' : seq.count('G'), 'C' : seq.count('C')}
FASTA.close()

for key in seqs:
  print(key, seqs[key]['A'], seqs[key]['T'], seqs[key]['G'], seqs[key]['C'])




















