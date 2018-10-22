#!/usr/bin/env python3

from Bio import SeqIO

fasta_dict = SeqIO.to_dict(SeqIO.parse('human_cds.fasta', 'fasta'))

print('SeqID', 'GC_content')
for record in fasta_dict:
   freq_A = fasta_dict[record].seq.count('A') / len(fasta_dict[record])
   freq_T = fasta_dict[record].seq.count('T') / len(fasta_dict[record])
   freq_G = fasta_dict[record].seq.count('G') / len(fasta_dict[record])
   freq_C = fasta_dict[record].seq.count('C') / len(fasta_dict[record])
   GC_content = (freq_G + freq_C) * 100
   GC_content = round(GC_content, 2)
   print(record, GC_content)


















 















