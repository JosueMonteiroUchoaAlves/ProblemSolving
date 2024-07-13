# https://leetcode.com/problems/daily-temperatures/description/

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        top = -1
        ind = 1
        stack = []
        answer =[0]* len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > stack[top][0]:
                    index_actual = stack.pop()[ind]
                    answer[index_actual] = index - index_actual
            stack.append([temp, index])
        return answer
