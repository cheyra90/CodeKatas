import math
from unittest import TestCase

"""
given a range of numbers, calculate any instances where the squares of the divisors of any numbers within the list sums to a square number

eg => 42: Divsors:  1,2,3,6,7,14,21,42
Divosors Squared:   1,4,9,36,49,196,441,1764
sum():              2500 => (sqrt(50))
"""


def is_square(posInt):
  if posInt == 1:
    return True
  x = posInt // 2
  seen = set([x])
  while x * x != posInt:
    x = (x + (posInt // x)) // 2
    if x in seen:
      return False
    seen.add(x)
  return True

def divisorGen(x):
  divList = []
  y = 1
  while y <= math.sqrt(x):
    if x % y == 0:
      divList.append(y)
      divList.append(int(x / y))
    y += 1
  return list(set(divList))


def list_squared(a, b):
  res = []
  for i in range(a, b):
    d = divisorGen(i)
    d = sum([x*x for x in d])
    if is_square(d):
      res.append([i, d])
  return res
