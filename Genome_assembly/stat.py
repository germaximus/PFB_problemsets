#!/usr/bin/env python3

from Bio import SeqIO


fasta_dict = SeqIO.to_dict(SeqIO.parse('ecoliPB-filtered_0.50.contigs.fasta', 'fasta'))


genome_size = 0
contig_stats = {}
contig_number = 0

for record in fasta_dict:
   contig_stats[str(len(fasta_dict[record].seq))] = record
   genome_size += len(fasta_dict[record].seq)
   contig_number += 1

contigs = list(contig_stats.keys())
for i in range(len(contigs)):  contigs[i] = int(contigs[i])

print('Shortest Contig ID:', contig_stats[str(min(contigs))], 'Nucleotide length', min(contigs))
print('Longest Contig ID:', contig_stats[str(min(contigs))], 'Nucleotide length', max(contigs))
print('Genome Size:', genome_size)

contigs.sort()
contigs.reverse()

counter = 0
n50 = 0
l50 = 0
for i in range(len(contigs)):
   counter += contigs[i]
   if counter >= (genome_size/2): 
      n50 = contigs[i]
      l50 = i
      break

print('N50: ', n50)
print('L50: ', l50)








   






















