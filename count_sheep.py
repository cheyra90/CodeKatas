'''
given 

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

count the amount of Trues

'''

arr = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

def count_sheep(arr):
  
  return arr.count(True) #Shorter implementation
  #return sum(1 for x in arr if x == True) # Longer implementation


x = count_sheep(arr)
print(x)