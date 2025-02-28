#https://www.hackerrank.com/challenges/flipping-bits/problem?isFullScreen=true

def flippingBits(n):
  n = bin(n)[2:].rjust(32, '0')
  print(n)
  res = ''
  for char in n:
    if char == '1':
      res += '0'
    else:
      res += '1'
  return int(res, 2)
print(flippingBits(3))
