#!/usr/bin/env python3
# Functions work on a sequence string, no headers or new lines allowed

# Calculate GC content
def percentGC (sequence):
  G_count = sequence.count('G')
  C_count = sequence.count('C')
  GC_content = (G_count + C_count) / len(sequence)
  return GC_content

# Reverse complement
def revComp_sequence (sequence):
  sequence = sequence.lower().replace('a','T').replace('t','A').replace('g','C').replace('c','G')
  sequence = sequence[::-1]
  return(sequence)











