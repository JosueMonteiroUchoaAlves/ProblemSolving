# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/?envType=problem-list-v2&envId=binary-search

from typing import List


def search(nums: List[int], target: int) -> bool:
    l, r = 0, len(nums)-1

    while l<=r:
        m = (l+r)//2
        
        if target == nums[m]:
            return True
        
        # para um caso como: [1,0,1,1,1] onde sei que:
        # não é m, e l é igual a m, então também não pode ser l! e como ele me confundiria eu apenas ando o ponteiro
        if nums[l] == nums[m]:
            l += 1
            continue
        
        if nums[l] < nums[m]:
            if target < nums[m]:
                if target >= nums[l]:
                    r = m-1
                else:
                    l = m+1
            else:
                l = m+1
        else:
            if target > nums[m]:
                if target > nums[r]:
                    r=m-1
                else:
                    l=m+1
            else:
                r=m-1
    return False  

print(search([1,0,1,1,1], 1))
print(search([1,0,1,1,1], 0))
