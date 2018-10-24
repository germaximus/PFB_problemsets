#!/usr/bin/env python3

import sys

FILE = open('reads.fq', 'r')
k_length = int(sys.argv[1])

kmers = {}
for line in FILE:
  header = line
  seq = next(FILE)
  seq = seq.rstrip()
  plus = next(FILE)
  quality = next(FILE)
  #sliding window
  for i in range(0, len(seq) - k_length + 1):
     kmer = seq[i:i + k_length]
     if kmer in kmers:  kmers[kmer] += 1
     else:  kmers[kmer] = 1

#sort kmers by frequency
kmers = sorted(kmers.items(), key = lambda x: x[1], reverse = True)
kmers = kmers[1:10]
for element in kmers:
  print (element[0], element[1])
   















