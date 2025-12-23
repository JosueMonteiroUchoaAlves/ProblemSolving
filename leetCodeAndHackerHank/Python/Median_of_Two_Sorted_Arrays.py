# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# 4. Median of Two Sorted Arrays

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
  beg, end = 0, len(nums1)-1
  # The best position until now (Starts with any number, will ever have a place)
  bestPos = -1
  for num in nums2:
    beg, end = 0, len(nums1)-1
  # The best position until now (Starts with any number, will ever have a place)
    bestPos = -1
    while beg<=end:
      mid = (beg+end)//2
      i = nums1[mid]
      if num >= nums1[mid]:
        beg=mid+1
        bestPos=mid+1 
        continue
      if num <= nums1[mid]:
        end=mid-1
        bestPos=mid
        continue
    nums1.insert(bestPos, num)
  evenList = len(nums1) % 2 == 0 
  midNum = len(nums1)/ 2
  if evenList:
    return (nums1[int(midNum-1)]+ nums1[int(midNum)])/2
  return nums1[int(midNum)]  
