# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/?envType=daily-question&envId=2025-09-08
# Not optimal solution (probably bc of the count function), but passed
from typing import List


def getNoZeroIntegers(n: int) -> List[int]:
    j= 1
    for j in range (1, n):
        if not str(j).count("0") and not str(n-j).count("0"):
            return [j, n-j]
print(getNoZeroIntegers(11))
