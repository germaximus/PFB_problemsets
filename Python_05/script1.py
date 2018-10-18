#!/usr/bin/env python3
#dictionaries and sets

my_dict = {'book' : 'Jetterbug Perfume', 'song' : "Tom Petty - I Won't Back Down", 'tree' : 'Cedar'}
print(my_dict['song'])

item = 'book'
print(my_dict[item])
print(my_dict['tree'])

my_dict['organism'] = 'Naked Mole Rat'
print(my_dict['organism'])

print('All possible keys:' +  '\t'.join(my_dict.keys()))
custom_input = input('Select a key to fetch a value for: ');
print(my_dict[custom_input])

custom_input1 = input('Select a key to change the value it holds: ')
custom_input2 = input('Type a new value for this key: ')
my_dict[custom_input1] = custom_input2
print('The new dictionary record is:', custom_input1, '=>', my_dict[custom_input1])

for i in my_dict:
  print(i, '=>', my_dict[i])












