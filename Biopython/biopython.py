#!/usr/bin/env python3

from Bio import SeqIO


sequence_counter = 0
nucleotide_counter = 0
sequence_lengths = []
GC_contents = []


for record in SeqIO.parse('Python_08.fasta', 'fasta'):
  #print('>' + record.description)
  #print('sequence', record.seq)
  sequence_counter += 1
  nucleotide_counter += len(record.seq)
  sequence_lengths.append(len(record.seq))
  GC_contents.append((record.seq.count('G') + record.seq.count('C')) / len(record.seq))



print('sequence count:', sequence_counter)
print('total number of nucleotides:', nucleotide_counter)
print('Average length:', nucleotide_counter / sequence_counter)
print('Shortest sequence:', min(sequence_lengths))
print('Longest sequence:', max(sequence_lengths))
print('Highest GC content:', max(GC_contents))
print('Lowest GC content:', min(GC_contents))














