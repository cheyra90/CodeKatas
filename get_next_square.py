'''
given a positive integer, return the next perfect square, if it is not a square number, return -1
'''

import math

x = 121


def next_square_alt(sq):
  root = sq ** 0.5
  if not root.is_integer():
    return -1
  return int((root + 1) ** 2)



def next_square(sq):
  if math.sqrt(sq) % 1 != 0:
    return -1
  return int((math.sqrt(sq) + 1) ** 2)

output = next_square(x)
output2 = next_square_alt(x)
print(output, output2)