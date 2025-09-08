# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1763220650/

def lengthOfLongestSubstring(s: str) -> int:
    ans = 0
    window = []
    pointer = 0
    sLength = len(s)
    
    while pointer < sLength:
        item = s[pointer]
        if item not in window:
            window.append(item)
            ans = max(len(window),ans)
            pointer += 1
        else:
            while item in window:
                window.pop(0)
            window.append(item)
            pointer += 1
    return ans
print(lengthOfLongestSubstring("pwwkew"))
