#!/usr/bin/env python3

items = ['R','Python','Perl','C','JavaScript']

print(items)     #print all elements
print(items[2])  #print middle element

items[2] = "icecream"
print(items)     #print a list with replacements 

items.append('Ruby')
items.insert(0, "Java")
items.insert(1,"Pascal")
print(items)

items.pop()      #remove last element
print(items)

items.pop(0)     #remove first element
print(items)

items.pop(1)     #remove an element from eleswhere
print(items)

print(','.join(items))

#-------   Sorting   ------------------

entry = 'sapience, erectus, neanderthalensis'
print(entry)

print(entry.split(', '))

items = entry.split(', ')
print(items)

items.sort()
print(items)

print(sorted(items, key=len)) #sort by length

#---------   Loops  -----------------------
# print numbers 1 to 100
counter = 1
while counter < 101:
 print(counter)
 counter += 1

#calculate factorial of 1000
counter = 1
factorial = 1
while counter <= 1000:
  factorial *= counter
  counter += 1
else: print(factorial)

#iterate through elements with regular for loop
items = [101,2,15,22,95,33,2,27,72,15,52]
for i in items:
  if(i % 2 == 0): print(i)

items.sort()
print(items)
cumsum_odd = 0
cumsum_even = 0
for i in items:
  print(i)
  if (i % 2 == 0):
    cumsum_even += i
  else:
    cumsum_odd += i
print('Sum of even elements is {}, sum of odd elements is {}'.format(cumsum_even, cumsum_odd))

#for loop with range
for i in range(100):
  print(i, end='\t')

#for loop with list comprehension
sequence = [i for i in range(100)]
print(sequence)









  






