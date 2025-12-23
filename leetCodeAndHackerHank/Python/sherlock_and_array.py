#https://www.hackerrank.com/challenges/sherlock-and-array/problem?isFullScreen=true

def balancedSums(arr):
  array_length = len(arr)
  left_sum = [0]* array_length
  right_sum = [0]* array_length
  for i in range(1, array_length):
    left_sum[i] = arr[i-1] + left_sum[i-1]
  for i in range(array_length-2, -1, -1):
    right_sum[i] = arr[i+1] + right_sum[i+1]
    if right_sum[i] == left_sum[i]:
      return 'YES'
  if right_sum[0] == left_sum[0]:
      return 'YES'
  return 'NO'

print(balancedSums([1, 2, 3])) #NO
