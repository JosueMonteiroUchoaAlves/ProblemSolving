# https://leetcode.com/contest/weekly-contest-405/problems/find-the-encrypted-string/

def getEncryptedString(s: str, k: int) -> str:
  answer = list(s)
  for i in range(len(s)):
    print((i+k)%len(s))
    answer[i] = s[(i+k)%len(s)]
  return ''.join(answer)

print(getEncryptedString("dart",3))
