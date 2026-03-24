# !/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER e
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s = start point
#

"""
    Se Edges[elemento][0] == s:
        distancia = 6
    senão:
        distancia = distancia[Edges[elemento][0]] + 6 que é a distancia do anterior a ele + 6
"""


def bfs(n, e, edges, s):
    relationships = [[] for _ in range(n)]
    for element in edges:
        relationships[element[0]-1].append(element[1])
        # elemento x se relaciona com y
    pilha = [s]
    visitado = [False for _ in range(n)]
    distancia = [-1 for _ in range(n)] 
    prev =distancia.copy()
    distancia[s-1] = 0
    prev[s-1] = s
    for elemento in pilha:
        visitado[elemento-1] = True
        for relacionado in relationships[elemento-1]:
            if not visitado[relacionado-1]:
                pilha.append(relacionado)
                prev[relacionado-1] = elemento
                if prev[relacionado-1]==s:
                    distancia[relacionado-1] = 6
                else:
                    distancia[relacionado-1] = distancia[prev[relacionado-1]-1] + 6 #distancia do elemento é a distancia do elemento anterior +6
    """print("prev:"+ str(prev) + "distancia:"+ str(distancia));
    for linha in visitado:
        print(linha)
    for relations in relationships:
        print(relations)"""
    distancia.pop(s-1)
    print(distancia)
    return distancia

print(bfs(3,1 ,[[2,3]],2))
"""
The enumerate() function is used to generate an iterator that produces pairs of (index, value) for 
each element in an iterable object. This means that instead of manually keeping track of the index 
using a separate variable, we can use the enumerate() function to obtain the index directly.

"""
