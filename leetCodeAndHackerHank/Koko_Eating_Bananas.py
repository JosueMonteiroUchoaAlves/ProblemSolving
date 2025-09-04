from typing import List

    
def minEatingSpeed(piles: List[int], h: int) -> int:
    biggestPile = max(piles)
    if h == len(piles):
        return biggestPile
    l, r = 1, biggestPile
    hoursTaken = 0
    answer = float('inf')
    while l <= r:
        m = (l + r) // 2     
        hoursTaken = 0
        for item in piles:
            arredondado =  int(item/m + 1) if item/m != int(item/m) else item/m
            hoursTaken += arredondado
        if hoursTaken <= h:
            answer = min(m, answer)
            # Quero o menor tempo possivel:
            r = m-1
            m = (l + r) // 2 
        else:
            l = m+1
    return answer
print(minEatingSpeed([30,11,23,4,20],6))
