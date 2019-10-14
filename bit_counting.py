'''
given  a non negative integer as input write a function to return the number of bits which are equal to one in the binary representation of that number. 

1234 => 10011010010 returns 5 due to 5 instances of 1
'''

number = 12385484

def count_bits(n):
  b = '{0:b}'.format(n)
  return len([x for x in b if x == '1'])

  #Alternatively this also works... and is better... and wasn't written by me
  # return bin(n).count('1')

print(count_bits(number))