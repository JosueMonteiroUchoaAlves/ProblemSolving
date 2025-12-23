#https://www.hackerrank.com/challenges/find-the-median/problem?isFullScreen=true
def findMedian(arr:list)->int:
    arr.sort()
    return arr[len(arr)//2]
print(findMedian([1,2,3]))
