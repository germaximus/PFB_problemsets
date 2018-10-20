#!/usr/bin/env python3
# Type Python_08.fasta as an input
# Split gene sequences into codons

import re
import sys

fasta = sys.argv[1]
FASTA = open(fasta, 'r')

seq = ''
gene_name = ''
gene_descr = ''

for line in FASTA:
  line = line.rstrip()
  match = re.search(r'(^>\S*)(\s*.*)', line)
  if match:
     if len(seq) > 0:
        rev_comp = seq.lower().replace('a','T').replace('t','A').replace('g','C').replace('c','G')
        rev_comp = rev_comp[::-1]
        print(gene_name + '-frame-1-codons')
        print(' '.join(re.findall(r'\w{1,3}', seq)))

        seq = seq[1:]
        print(gene_name + '-frame-2-codons')
        print(' '.join(re.findall(r'\w{1,3}', seq)))

        seq = seq[1:]
        print(gene_name + '-frame-3-codons')
        print(' '.join(re.findall(r'\w{1,3}', seq)))

        print(gene_name + '-revcomp-frame-1-codons')
        print(' '.join(re.findall(r'\w{1,3}', rev_comp)))

        rev_comp = rev_comp[1:]
        print(gene_name + '-revcomp-frame-2-codons')
        print(' '.join(re.findall(r'\w{1,3}', rev_comp)))
        
        rev_comp = rev_comp[1:]
        print(gene_name + '-revcomp_frame-3-codons')
        print(' '.join(re.findall(r'\w{1,3}', rev_comp)) )
        seq = ''
     gene_name = match.group(1).lstrip('>')
     gene_descr = match.group(2)
  else:
    seq = seq + line


rev_comp = seq.lower().replace('a','T').replace('t','A').replace('g','C').replace('c','G')
rev_comp = rev_comp[::-1]
print(gene_name + '-frame-1-codons')
print(' '.join(re.findall(r'\w{1,3}', seq)))

seq = seq[1:]
print(gene_name + '-frame-2-codons')
print(' '.join(re.findall(r'\w{1,3}', seq)))

seq = seq[1:]
print(gene_name + '-frame-3-codons')
print(' '.join(re.findall(r'\w{1,3}', seq)))

print(gene_name + '-revcomp-frame-1-codons')
print(' '.join(re.findall(r'\w{1,3}', rev_comp)))

rev_comp = rev_comp[1:]
print(gene_name + '-revcomp-frame-2-codons')
print(' '.join(re.findall(r'\w{1,3}', rev_comp)))

rev_comp = rev_comp[1:]
print(gene_name + '-revcomp_frame-3-codons')
print(' '.join(re.findall(r'\w{1,3}', rev_comp)) )
 
FASTA.close()







