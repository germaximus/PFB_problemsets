#!/usr/bin/env python3

import re

FILE = open('bowtie2.sam', 'r')

expression = {}
for line in FILE:
  line = line.split('\t')
  read_name = line[0]
  gene_name = re.search(r'(.*)[\^]', line[2]).group(1)

  if gene_name in expression: expression[gene_name].add(read_name)
  else: expression[gene_name] = set()

expression = sorted(expression.items(), key = lambda x: len(x[1]), reverse = True)
for element in expression: print(element[0], len(element[1]))




















