# https://leetcode.com/contest/weekly-contest-466/problems/minimum-operations-to-transform-string/

def minOperations(s: str) -> int:
    sList = sorted(list(s))
    alphabetMap = {letter:abs(index-25)+1 if letter != "a" else 0 for index, letter in enumerate(list("abcdefghijklmnopqrstuvwxyz"))}
    ans = 0
    for item  in sList:
        ans  = max(ans, alphabetMap[item])
    return ans

print(minOperations("b"))
