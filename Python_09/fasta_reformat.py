#!/usr/bin/env python3
#Takes a fasta file with multiple records and re-formats each record to the desired length

import re
import argparse

def formatter(dna, width = 60):
  output = re.split(r'\n+', dna)
  output = ''.join(output)
  pattern = r'\w{1,' + str(width) + r'}'
  output = re.findall(pattern, output)
  output = '\n'.join(output)
  return output

parser = argparse.ArgumentParser('Takes a fasta file and re-format')
parser.add_argument('fasta', type = str, help = 'input fasta file')
parser.add_argument('width', type = int, help = 'new length of the line to re-format')
args = parser.parse_args()

fasta = args.fasta
width = args.width

if not fasta.endswith(('.fasta', '.fa')): raise ValueError('Input file is not in a fasta format')

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
       print('>' +  gene_name + gene_descr)
       print(formatter(dna = seq, width = width))
       seq = ''
    gene_name = match.group(1).lstrip('>')
    gene_descr = match.group(2)
  else:
     seq = seq + line
 
print('>' + gene_name + gene_descr)
print(formatter(dna = seq, width = width))
FASTA.close()




