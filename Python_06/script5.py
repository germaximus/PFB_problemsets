#!/usr/bin/env python3

PROLIF = open('alpaca_stemcellproliferation_genes.tsv','r')
TR_FACT = open('alpaca_transcriptionFactors.tsv','r')

prolif = set()
tr_fact = set()

counter = 0
for line in PROLIF:
 counter += 1
 if counter != 1:
   line = line.rstrip()
   prolif.add(line)
PROLIF.close()

counter = 0
for line in TR_FACT:
 counter += 1
 if counter != 1:
   line = line.rstrip()
   tr_fact.add(line)
TR_FACT.close()

overlap = prolif & tr_fact
print('Overlap between Proliferation and Transcription Factor genes')
for i in overlap: print(i)


















