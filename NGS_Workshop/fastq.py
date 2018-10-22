#!/usr/bin/env python3

INPUT = open('four_reads.fastq', 'r')

good_quality_counter = 0
total_nucl = 0
for line in INPUT:
  header = line.rstrip()
  sequence = next(INPUT).rstrip()
  plus = next(INPUT).rstrip()
  quality = next(INPUT).rstrip()
  total_nucl += len(quality)
  
  for character in quality:
      if ord(character) - 33 > 30:
        good_quality_counter += 1

  sequence_list = list(sequence)
  quality_list = list(quality)
  
  for i in range(len(quality_list)):
      if ord(quality_list[i]) - 33 <= 30:
         quality_list[i] = '*'
         sequence_list[i] = '*'

  masked_sequence = ''.join(sequence_list)
  masked_quality = ''.join(quality_list)
  if len(masked_quality) != len(masked_sequence): raise ValueError('Length of the sequence is nor equal to length of the quality score after trimming')
 
  masked_sequence_5trim = masked_sequence.lstrip('*')
  masked_quality_5tim = masked_quality.lstrip('*')
  masked_sequence_3trim = masked_sequence.rstrip('*')
  masked_quality_3trim = masked_quality.rstrip('*')

  new_sequence = sequence[len(sequence) - len(masked_sequence_5trim) : len(masked_sequence_3trim) + 1]
  new_quality = quality[len(quality) - len(masked_sequence_5trim) : len(masked_quality_3trim) + 1]
 
  print(header)
  print(new_sequence)
  print(plus)
  print(new_quality)

#good_qual_fraction = good_quality_counter/total_nucl * 100
#print('Fraction of nucleotides with quality score greater than 30:', round(good_qual_fraction, 2))























