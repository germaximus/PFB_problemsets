#!/usr/bin/env python3

def rc(sequence):
  return  sequence.replace('a','T').replace('t','A').replace('g','C').replace('c','G')[::-1].lower()

def align(sequence1, sequence2, match = 1, mismatch = -1):
  if len(sequence1) != len(sequence2): raise ValueError('Input sequences should be of the same length!')

  score = 0
  for a in range(len(sequence1)):
     if sequence1[a] == sequence2[a]: score += match
     else: score += mismatch
  return score

print('Scores with match = 1 and mismatch = -1 parameters')
print(align(sequence1 = 'agtctgtca', sequence2 = 'gatctctgc'))
print(align(sequence1 = rc('agtctgtca'), sequence2 = 'gatctctgc'))
print(align(sequence1 = 'agtctgtca', sequence2 = rc('gatctctgc')))
print(align(sequence1 = rc('agtctgtca'), sequence2 = rc('gatctctgc')))

print('Scores with match = 2 and mismatch = -2 parameters')
print(align(sequence1 = 'agtctgtca', sequence2 = 'gatctctgc', match = 2, mismatch = -2))
print(align(sequence1 = rc('agtctgtca'), sequence2 = 'gatctctgc', match = 2, mismatch = -2))
print(align(sequence1 = 'agtctgtca', sequence2 = rc('gatctctgc'), match = 2, mismatch = -2))
print(align(sequence1 = rc('agtctgtca'), sequence2 = rc('gatctctgc'), match = 2, mismatch = -2))










