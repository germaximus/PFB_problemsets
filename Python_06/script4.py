#!/usr/bin/env python3
lpaca_stemcellproliferation_genes.tsv
ALL_GENES = open('alpaca_all_genes.tsv', 'r')
PROLIF = open('alpaca_stemcellproliferation_genes.tsv','r')
PIGM = open('alpaca_pigmentation_genes.tsv','r')

all_genes = set()
prolif = set()
pigm = set()

counter = 0
for line in ALL_GENES:
  counter += 1
  if counter != 1:
    line = line.rstrip()
    all_genes.add(line)
ALL_GENES.close()

counter = 0    
for line in PROLIF:
  counter += 1
  if counter != 1:
    line = line.rstrip()
    prolif.add(line)
PROLIF.close()

counter = 0
for line in PIGM:
  counter += 1
  if counter != 1:
    line = line.rstrip()
    pigm.add(line)
PIGM.close()


overlap = pigm & prolif
print('Overlap between Proliferation and Pigment genes')
for i in overlap: print(i)











