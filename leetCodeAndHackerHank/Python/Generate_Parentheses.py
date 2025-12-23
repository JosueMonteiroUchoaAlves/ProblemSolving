# https://leetcode.com/problems/generate-parentheses/submissions/1758199050/
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parentheses = []
        answer = []
        def backtraking( parenthesesStack: list, aberturas: int, fechamentos: int, answer:list):
            if (aberturas == fechamentos) and aberturas == n:
                answer.append("".join(parenthesesStack.copy()))
                return answer

            if aberturas < n:
                parenthesesStack.append("(")
                aberturas += 1
                backtraking(parenthesesStack, aberturas, fechamentos, answer)
                parenthesesStack.pop()
                aberturas -= 1
            if aberturas > fechamentos:
                parenthesesStack.append(")")
                fechamentos += 1
                backtraking(parenthesesStack, aberturas, fechamentos, answer)
                parenthesesStack.pop()
                fechamentos -= 1
        backtraking(parentheses, 0, 0, answer)
        return answer

S = Solution()
print(S.generateParenthesis(3))
