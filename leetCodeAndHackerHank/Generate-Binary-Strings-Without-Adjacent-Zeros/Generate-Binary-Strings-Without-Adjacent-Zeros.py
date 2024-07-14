# https://leetcode.com/contest/weekly-contest-405/problems/generate-binary-strings-without-adjacent-zeros/description/

def validStrings (n: int) -> list[str]:
    stack = []
    ans = []
    
    def createString():
      if len(stack) == n:
        ans.append(''.join(stack))
        return
      if not stack or stack[-1] == "1":
        stack.append("0")
        createString()
        stack.pop()
        
      stack.append("1")
      createString()
      stack.pop()
      
    createString()
    return ans
print(validStrings(3))
