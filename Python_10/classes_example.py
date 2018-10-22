#!/usr/bin/env python3

import re

class DNAseq (object):
  def __init__(self, sequence, name, origin):
    self.sequence = sequence
    self.name = name
    self.origin = origin
  
  def findLength(self):
    return len(self.sequence)
 
  def nucl_comp(self):
    percent_A = self.sequence.count('A') / len(self.sequence)
    percent_T = self.sequence.count('T') / len(self.sequence)
    percent_G = self.sequence.count('G') / len(self.sequence)
    percent_C = self.sequence.count('C') / len(self.sequence)
    return '\nPercentage of As: ' + str(percent_A) + '\nPercentage of Ts: ' + str(percent_T) + '\nPercentage of Gs: ' + str(percent_G) + '\nPercentage of Cs: ' + str(percent_C)
    
  def GC_content(self):
     GC_content = (self.sequence.count('G') + self.sequence.count('C')) / len(self.sequence)
     return GC_content

  def fastaFormat(self, width = 60):
     formatted_sequence = re.findall(r'\w{1,'+ str(width) +r'}', self.sequence)
     formatted_sequence = '\n'.join(formatted_sequence)
     return  '>' + self.name + '\n' + formatted_sequence

  def compare(self, second_record = {}):
     if self.sequence == second_record['sequence'] and self.name == second_record['name'] and self.origin == second_record['origin']: return True
     else: return False



record = DNAseq(sequence = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCT', name = 'geneABC', origin = 'My mind')

#record = DNAseq(sequence = 'ATGC', name = 'geneABC', origin = 'My mind')


print('Sequence contained in the record:', record.sequence)
print('Record name:', record.name)
print('Record origin:', record.origin)
print('Sequence length:', record.findLength())
print('Nucleotide composition:', record.nucl_comp())
print('GC content:', record.GC_content())
print('FASTA formatted output:\n' + record.fastaFormat(width=40))
print('Two sequences are identical: ', record.compare(second_record = {'name' : 'geneABC', 'origin' : 'My mind', 'sequence' : 'ATGC' }))













