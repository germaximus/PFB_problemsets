#!/usr/bin/env python3

IN = open('Python_06.fastq', 'r')
line_counter = 0
char_counter = 0
for line in IN:
 line = line.rstrip()
 line_counter += 1
 char_counter += len(line)
IN.close()

average_length = char_counter / line_counter

print('Number of lines:', line_counter)
print('Number of characters:', char_counter)
print('Average line length:', average_length)














