# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

def evalRPN(tokens: list[str]) -> int:
  operacoes = {"+":1,"-":2,"*":3,"/":4}
  outralista=[] 
  for item in tokens:
    if i:= operacoes.get(item, 0):
      if i == 1:  
        outralista.append(int(outralista.pop())+int(outralista.pop()))
      if i == 2:  
        outralista.append(int(outralista.pop())-int(outralista.pop()))
      if i == 3:  
        outralista.append(int(outralista.pop())*int(outralista.pop()))
      if i == 4:  
        outralista.append(int(int(outralista.pop(-2))/int(outralista.pop())))
    else:
      outralista.append(item)
  return outralista

