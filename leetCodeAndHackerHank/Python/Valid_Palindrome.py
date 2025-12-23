# https://leetcode.com/problems/valid-palindrome/submissions/1322367891/
# 125. Valid Palindrome

def isPalindrome(s: str) -> bool:
  s = ''.join(char for char in s if char.isalnum()).lower()
  a,z = 0,len(s)-1
  while a < z:
    if s[a] != s[z]:
      return False
    a +=1
    z -=1
  return True
