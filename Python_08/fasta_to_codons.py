#!/usr/bin/env python3
# Type Python_08.fasta as an input

import re
import sys

def translate(seq):
   codons = re.findall(r'\w{1,3}', seq) 
   translation = ''
   for codon in codons:
      if len(codon) == 3: 
        aa = translation_table[codon]
        translation = translation + aa
   return(translation)


fasta = sys.argv[1]
FASTA = open(fasta, 'r')
CODON = open('Python_08.codons-6frames.nt', 'w')
TRANSLATION = open('Python_08.translated.aa', 'w')
LONGEST = open('Python_08.translated-longest.aa', 'w')

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}

seq = ''
gene_name = ''
gene_descr = ''

for line in FASTA:
  line = line.rstrip()
  match = re.search(r'(^>\S*)(\s*.*)', line)
  if match:
     if len(seq) > 0:
        longest_peptide = ''
        rev_comp = seq.lower().replace('a','T').replace('t','A').replace('g','C').replace('c','G')
        rev_comp = rev_comp[::-1]

        CODON.write(gene_name + '-frame-1-codons\n')
        CODON.write(' '.join(re.findall(r'\w{1,3}', seq)) + '\n' )
        TRANSLATION.write(gene_name + '-frame-1-translation\n')
        TRANSLATION.write(translate(seq) + '\n')
        peptides = re.findall(r'(M.*?)\*', translate(seq))
        for peptide in peptides: 
          if len(peptide) > len(longest_peptide): longest_peptide = peptide

        seq = seq[1:]
        CODON.write(gene_name + '-frame-2-codons\n')
        CODON.write(' '.join(re.findall(r'\w{1,3}', seq)) + '\n' )
        TRANSLATION.write(gene_name + '-frame-2-translation\n')
        TRANSLATION.write(translate(seq) + '\n')
        peptides = re.findall(r'(M.*?)\*', translate(seq))
        for peptide in peptides: 
          if len(peptide) > len(longest_peptide): longest_peptide = peptide

        seq = seq[1:]
        CODON.write(gene_name + '-frame-3-codons\n')
        CODON.write(' '.join(re.findall(r'\w{1,3}', seq)) + '\n')
        TRANSLATION.write(gene_name + '-frame-3-translation\n')
        TRANSLATION.write(translate(seq) + '\n')
        peptides = re.findall(r'(M.*?)\*', translate(seq))
        for peptide in peptides: 
          if len(peptide) > len(longest_peptide): longest_peptide = peptide

        CODON.write(gene_name + '-revcomp-frame-1-codons\n')
        CODON.write(' '.join(re.findall(r'\w{1,3}', rev_comp)) + '\n' )
        TRANSLATION.write(gene_name + 'revcomp-frame-1-translation\n')
        TRANSLATION.write(translate(rev_comp) + '\n')
        peptides = re.findall(r'(M.*?)\*', translate(rev_comp))
        for peptide in peptides: 
          if len(peptide) > len(longest_peptide): longest_peptide = peptide

        rev_comp = rev_comp[1:]
        CODON.write(gene_name + '-revcomp-frame-2-codons\n')  
        CODON.write(' '.join(re.findall(r'\w{1,3}', rev_comp)) + '\n' )
        TRANSLATION.write(gene_name + '-revcomp-frame-2-translation\n')
        TRANSLATION.write(translate(rev_comp) + '\n')
        peptides = re.findall(r'(M.*?)\*', translate(rev_comp))
        for peptide in peptides: 
          if len(peptide) > len(longest_peptide): longest_peptide = peptide

        rev_comp = rev_comp[1:]
        CODON.write(gene_name + '-revcomp_frame-3-codons\n')
        CODON.write(' '.join(re.findall(r'\w{1,3}', rev_comp)) + '\n' )
        TRANSLATION.write(gene_name + '-revcomp-frame-3-translation\n')
        TRANSLATION.write(translate(rev_comp) + '\n')
        peptides = re.findall(r'(M.*?)\*', translate(rev_comp))
        for peptide in peptides: 
          if len(peptide) > len(longest_peptide): longest_peptide = peptide
        
        LONGEST.write(gene_name + '\n')
        LONGEST.write(longest_peptide + '\n')
        seq = ''
     gene_name = match.group(1).lstrip('>')
     gene_descr = match.group(2)
  else:
    seq = seq + line

longest_peptide = ''
rev_comp = seq.lower().replace('a','T').replace('t','A').replace('g','C').replace('c','G')
rev_comp = rev_comp[::-1]
CODON.write(gene_name + '-frame-1-codons\n')
CODON.write(' '.join(re.findall(r'\w{1,3}', seq)) + '\n')
TRANSLATION.write(gene_name + '-frame-1-translation\n')
TRANSLATION.write(translate(seq) + '\n')
peptides = re.findall(r'(M.*?)\*', translate(seq))
for peptide in peptides: 
   if len(peptide) > len(longest_peptide): longest_peptide = peptide


seq = seq[1:]
CODON.write(gene_name + '-frame-2-codons\n')
CODON.write(' '.join(re.findall(r'\w{1,3}', seq)) + '\n')
TRANSLATION.write(gene_name + '-frame-2-translation\n')
TRANSLATION.write(translate(seq) + '\n')
peptides = re.findall(r'(M.*?)\*', translate(seq))
for peptide in peptides: 
   if len(peptide) > len(longest_peptide): longest_peptide = peptide


seq = seq[1:]
CODON.write(gene_name + '-frame-3-codons\n')
CODON.write(' '.join(re.findall(r'\w{1,3}', seq)) + '\n')
TRANSLATION.write(gene_name + '-frame-3-translation\n')
TRANSLATION.write(translate(seq) + '\n')
peptides = re.findall(r'(M.*?)\*', translate(seq))
for peptide in peptides: 
   if len(peptide) > len(longest_peptide): longest_peptide = peptide


CODON.write(gene_name + '-revcomp-frame-1-codons\n')
CODON.write(' '.join(re.findall(r'\w{1,3}', rev_comp)) + '\n')
TRANSLATION.write(gene_name + '-revcomp_frame-1-translation\n')
TRANSLATION.write(translate(rev_comp) + '\n')
peptides = re.findall(r'(M.*?)\*', translate(rev_comp))
for peptide in peptides: 
   if len(peptide) > len(longest_peptide): longest_peptide = peptide


rev_comp = rev_comp[1:]
CODON.write(gene_name + '-revcomp-frame-2-codons\n')
CODON.write(' '.join(re.findall(r'\w{1,3}', rev_comp)) + '\n' )
TRANSLATION.write(gene_name + '-revcomp_frame-2-translation\n')
TRANSLATION.write(translate(rev_comp) + '\n')
peptides = re.findall(r'(M.*?)\*', translate(rev_comp))
for peptide in peptides: 
   if len(peptide) > len(longest_peptide): longest_peptide = peptide


rev_comp = rev_comp[1:]
CODON.write(gene_name + '-revcomp_frame-3-codons\n')
CODON.write(' '.join(re.findall(r'\w{1,3}', rev_comp)) + '\n' )
TRANSLATION.write(gene_name + '-revcomp-frame-3-translation\n')
TRANSLATION.write(translate(rev_comp) + '\n')
peptides = re.findall(r'(M.*?)\*', translate(rev_comp))
for peptide in peptides: 
   if len(peptide) > len(longest_peptide): longest_peptide = peptide


FASTA.close()
CODON.close()
TRANSLATION.close()
LONGEST.close()





