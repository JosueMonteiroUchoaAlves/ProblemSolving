possibilities = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"

## CODE FULLY WORKING

querysNumber = int(input())
awswers = []
for _ in range(querysNumber):
  code = input()
  i = int(input())
  decifred = "".join([possibilities[possibilities.find(char)-i+26] for char in code])
  awswers.append(decifred)

print('\n'.join(map(str, awswers)))
