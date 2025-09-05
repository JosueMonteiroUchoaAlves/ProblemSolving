# https://leetcode.com/problems/sqrtx/description/?envType=problem-list-v2&envId=binary-search

def mySqrt(x: int) -> int:
    l, r = 0, x
    
    if x == 1:
        return 1
    if x == 2:
        return 1
    if x == 3:
        return 1
    
    resultado = 0
    
    while l <= r:
        m = (l + r) // 2
        
        difference = ((m*m) - x)
        if (difference <= 0) and (difference >= -(x/2)):
            resultado = max(resultado, m)
        if difference > 0:
            # é porque o m*m é maior que x, então tenho que diminuir m
            r = m-1
        else:
            l = m+1
    return resultado

print(mySqrt(36))
print(mySqrt(8))
