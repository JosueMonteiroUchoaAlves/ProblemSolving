# https://leetcode.com/problems/search-insert-position/?envType=problem-list-v2&envId=binary-search

from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1
    m = 0
    while l<=r:
        m =(l+r)//2
        
        if target == nums[m]:
            return m
        
        if target < nums[m]:
            r=m-1
            continue
        
        if target > nums[m]:
            l=m+1

    """
    se target for maior que o numero final, indice dele seria m+1
    se target for menor que o final, o indice dele seria m pois o 
    que esta agora em m e todos os posteriores andariam 1 index para frente
    """
    return m+1 if target > nums[m] else m

print(searchInsert([1,3,5,6], 5))
