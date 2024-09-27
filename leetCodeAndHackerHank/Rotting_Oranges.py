# https://leetcode.com/problems/rotting-oranges/
# 994. Rotting Oranges

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
      linhas, colunas = len(grid), len(grid[0])
      rottenOranges = []
      global freshOranges
      freshOranges = 0
      visited = set()
      
      def addProxLaranja(l, c):
        global freshOranges
        if l not in range(linhas) or c not in range(colunas) or grid[l][c] != 1 or (l, c) in visited: return
        visited.add((l,c))
        rottenOranges.append([l, c])
        freshOranges -= 1
        return
      
      for linha in range(linhas):
        for coluna in range(colunas):
          if grid[linha][coluna] == 2:
            rottenOranges.append([linha, coluna])
          if grid[linha][coluna] == 1:
            freshOranges += 1
            
      time = 0
      directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # direita, baixo, esquerda, cima
      
      while rottenOranges and freshOranges:
        camada = len(rottenOranges)
        for _ in range(camada):
          rotOrange = rottenOranges.pop(0)
          l, c = rotOrange
          for direction in directions:
            adj_l = l + direction[0]
            adj_c = c + direction[1]
            addProxLaranja(adj_l, adj_c)
        time += 1
      return time if freshOranges == 0 else -1
