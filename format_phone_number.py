'''
given a list of 10 digits [1,2,3,4,5,6,7,8,9,0] format it into an american phone number format => (123) 456-7890
'''


test = [8,8,4,5,6,1,2,3,4,0]


def my_format_number(n):
  #I'm actually stupid...
  return ''.join('('+str(n[0:3])+')*'+str(n[3:6])+'-'+str(n[6:])).replace('[','').replace(']','').replace(' ','').replace(',','').replace('*',' ')

def format_number(n):
  return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)

print(*test) #How to unpack a list


n1 = my_format_number(test)
n2 = my_format_number(test)

print(n1, n2)