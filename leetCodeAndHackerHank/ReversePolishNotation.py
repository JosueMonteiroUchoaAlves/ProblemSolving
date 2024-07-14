# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

def evalRPN(tokens: list[str]) -> int:
  operations = {"+":1,"-":2,"*":3,"/":4}
  result=[] 
  for item in tokens:
    if i:= operations.get(item, 0):
      if i == 1:  
        result.append(int(result.pop())+int(result.pop()))
      if i == 2:  
        result.append(int(result.pop())-int(result.pop()))
      if i == 3:  
        result.append(int(result.pop())*int(result.pop()))
      if i == 4:  
        result.append(int(int(result.pop(-2))/int(result.pop())))
    else:
      result.append(item)
  return result

