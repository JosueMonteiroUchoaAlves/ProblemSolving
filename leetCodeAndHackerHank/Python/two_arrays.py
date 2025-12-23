# https://www.hackerrank.com/challenges/two-arrays/problem?isFullScreen=true
def twoArrays(k, A:list, B:list):
    A.sort()
    B.sort()
    for i in range(len(A)): 
      item1 = A[i]
      for j in range(len(B)):
        item2 = B[j]
        if item1 + item2 >= k:
          B.pop(j)
          break
      else:
        return "NO"
    return "YES"
print(twoArrays(10, [2, 1, 3],[7, 8, 9]))
