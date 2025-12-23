# https://leetcode.com/problems/search-a-2d-matrix/description/
# 74. Search a 2D Matrix

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
  min_, max_ = 0, len(matrix)-1
  mid_Column = (max_-min_)//2
  first_value, last_value = 0,0
  while min_ <= max_:
    first_value, last_value = matrix[mid_Column][0], matrix[mid_Column][-1]
    if first_value <= target and last_value >= target:
      break
    if last_value < target:
      min_ = mid_Column + 1
    if first_value > target:
      max_ = mid_Column - 1
    mid_Column = (max_+min_)//2
  else:
    # If do not complete the loop
    return False
  search_column = mid_Column
  min_, max_ = 0, len(matrix[search_column])-1
  mid_Column = (max_-min_)//2
  while min_ <= max_:
    if matrix[search_column][mid_Column]==target:
      return True
    if matrix[search_column][mid_Column] < target:
      min_ = mid_Column + 1
    elif matrix[search_column][mid_Column] > target:
      max_ = mid_Column - 1
    mid_Column = (max_+min_)//2
  return False
      
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
