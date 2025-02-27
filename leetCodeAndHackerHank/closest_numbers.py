# https://www.hackerrank.com/challenges/closest-numbers/problem?isFullScreen=true
def closestNumbers(arr):
  arr.sort()
  min_diff = float('inf')
  closest_numbers = []
  for i in range(1, len(arr)):
    diff = arr[i] - arr[i - 1]
    if diff < min_diff:
      closest_numbers = [arr[i - 1],arr[i]]
      min_diff = diff
      continue

    if diff == min_diff:
      closest_numbers.extend([arr[i - 1],arr[i]])
  return closest_numbers

print(closestNumbers([1,2,3,4,5]))
