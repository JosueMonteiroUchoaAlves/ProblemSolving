# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        combination = []
        answer = []
        def backtraking(map:map, digits:int, iterationDigit:int,iterationDigitLetter:int, answerList:list, combination:list):
            lettersOfThisDigit = map[digits[iterationDigit]]
            for letter in lettersOfThisDigit:
                combination.append(letter)
                if iterationDigit < len(digits)-1:
                    iterationDigit += 1
                    backtraking(map, digits, iterationDigit, iterationDigitLetter, answerList, combination)
                    iterationDigit -= 1 # voltando para o digito anterior
                    combination.pop() # removendo a letra desse digito
                else:
                    answerList.append("".join(combination.copy()))
                    combination.pop()
                        
        if not digits:
            return []
        backtraking(letterMap, digits, 0, 0, answer, combination)
        return answer
S = Solution()
print(S.letterCombinations("23"))
