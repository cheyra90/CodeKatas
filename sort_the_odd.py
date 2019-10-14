'''
  you have an array of numbers, sort ascending all the odd numbers and leave the even numbers  in place eg

  arr = [5,3,2,8,1,4] => [1,3,2,8,5,4]
'''


arr = [5,3,2,8,1,4]

def sort_odds(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
  

sorted_arr = sort_odds(arr)
print(sorted_arr)