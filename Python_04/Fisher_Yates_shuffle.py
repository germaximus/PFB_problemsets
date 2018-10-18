#!/usr/bin/env python3
#Fisher-Yates shuffle

import random

sequence = input('Enter DNA sequence ')
sequence = list(sequence)
length = len(sequence)

for i in range(length):
  position_A = random.randrange(length)
  position_B = random.randrange(length)
  nt_at_posA = sequence[position_A]
  sequence[position_A] = sequence[position_B]
  sequence[position_B] = nt_at_posA
  print('Step', i+1,''.join(sequence))











