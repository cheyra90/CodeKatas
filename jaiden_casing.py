'''
Jaiden Smith is known for capitalizing every word in a sentence, given a new sentence, return the Jaiden Cased sentence.

"The big red dog" ==> "The Big Red Dog"
'''



s = 'Peter piper picked a peck of pickled peppers'

def jaiden_case_1(string):
  words = [w for w in string.split(' ')]
  return ' '.join([c[0].upper() + c[1:] for c in words])


def jaiden_case_2(string):
  return " ".join(w.capitalize() for w in string.split())



j_case1 = jaiden_case_1(s)
j_case2 = jaiden_case_2(s)

print(j_case1, j_case2)