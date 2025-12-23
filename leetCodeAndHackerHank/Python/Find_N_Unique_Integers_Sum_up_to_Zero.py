# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/submissions/1762838694/?envType=daily-question&envId=2025-09-07
from typing import List


def sumZero(n: int) -> List[int]:
    ans = []
    total = 0
    index = 1
    if n%2!=0:
        ans.append(0)
    while len(ans) < n:
        if total != 0:
            total -= ans[-1]
            ans.append(-(ans[-1]))
            continue
        
        ans.append(index)
        total += index
        index += 1
    return ans

print(sumZero(4))
