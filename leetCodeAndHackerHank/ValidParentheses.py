# https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        possibilities = {'{':'}','[':']','{':'}','(':')'}
        stack = []
        for bracket in s:
            if bracket in ['{','[','(']:
                stack.append(bracket)
            elif stack and possibilities[stack[-1]] == bracket: 
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        return False
