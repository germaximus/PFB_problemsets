#!/usr/bin/env python3

print('printing list')
items = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for i in items:
  print(str(len(i)) + '\t' + i )

print('Now printing tuples')
my_tuples = [(len(i),i) for i in items]
for t in my_tuples:
  print(str(t[0]) + '\t' + t[1])

print('Now back to lists')
for i in items:
  print(str(items.index(i)) + '\t' + str(len(i)) + '\t' + i )




