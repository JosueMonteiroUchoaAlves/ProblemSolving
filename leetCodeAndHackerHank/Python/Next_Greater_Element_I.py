# https://leetcode.com/problems/next-greater-element-i/description/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {num:index for index, num in enumerate(nums1)}
        stack = []
        answer = [-1]*len(nums1)
        
        for num in nums2:
            if stack and num > stack[-1] :
                while stack and num > stack[-1]:
                    numb = stack.pop()
                    answer[hashmap[numb]] = num
            if num in hashmap.keys():
                stack.append(num)
        return answer
