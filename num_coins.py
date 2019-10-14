

def gcd(a,b):
  while b > 0:
    a, b = b, a % b
  return a

def lcm(a, b):
  return a*b / gcd(a,b)

print(int(lcm(12,64)))

def num_coins(pence):
  if pence < 1:
    return 0
  
  coins = [50,20,10,5,2,1]
  nc = 0
  for coin in coins:
    nc += pence/coin
    pence = pence / coin
    if pence == 0:
      break
  return nc

print(num_coins(52))