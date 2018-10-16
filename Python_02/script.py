#!/usr/bin/env python3
# fooling around with numbers and nested conditions
import sys

value = float(sys.argv[1])

if value > 0:
  if value < 50:
    if value % 2 == 0:
      print("The value is positive, less than 50 and even")
    else:
      print("The value is positive, less than 50 and odd")
  elif value > 50:
    if value % 3 == 0:
      print("The value is positive, larger than 50 and divisible by 3")
    else:
      print("The value is positive, larger than 50 and not divisible by 3")
  else: 
   print("The value is positive and equal to 50")
elif value < 0:
  print("The value is negative")
else:
  print("The value is 0")


# fooling around with indentations
# tabls and spaces cannot be mixed in the entire file, not only in a single script
if value > 0: print("test1")
else: print("test2_complete")

