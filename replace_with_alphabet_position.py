'''
  given a string, replace every letter with its position in the alphabet eg

  The => '20 8 5'
'''


test_string = "The sunset sets at twelve o' clock." 


def alphabet_position(text):
  l = [ord(l.lower())-96 for l in text if l.isalpha()]
  return ' '.join(map(str, l))

l = alphabet_position(test_string)
print(l)