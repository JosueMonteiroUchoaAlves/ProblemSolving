# https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
      self.Values = []
      self.min_stack = []

    def push(self, val: int) -> None:
      if not self.min_stack or val <= self.min_stack[-1]:
        self.min_stack.append(val)
      self.Values.append(val)

    def pop(self) -> None:
      if self.min_stack[-1] == self.Values.pop():
        self.min_stack.pop()

    def top(self) -> int:
      return self.Values[-1]

    def getMin(self) -> int:  
      return self.min_stack[-1]
    