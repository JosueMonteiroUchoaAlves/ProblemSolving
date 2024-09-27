# https://leetcode.com/problems/max-area-of-island/
# 695. Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
      maxArea = 0
      rows, columns = len(grid), len(grid[0])
      visited = set()
      
      def bfs(l, c):
        directions = [[0,-1],[-1, 0],[0, 1], [1, 0]] #esquerda, cima, direita, baixo
        queue = [[l,c]]
        tamanho_da_ilha = 0
        visited.add((l,c)) #adiciona o que eu vou estudar agora

        while queue:
          tamanho_da_ilha += 1
          estudando = queue.pop(0) # estudando as proximidades dessa "casa"
          l, c = estudando
          
          for direction in directions:
            linha_possivel = l + direction[0]
            coluna_possivel = c + direction[1]
            
            if linha_possivel not in range(rows) or coluna_possivel not in range(columns) or (linha_possivel, coluna_possivel) in visited or grid[linha_possivel][coluna_possivel] == 0: continue
            
            visited.add((linha_possivel,coluna_possivel))
            queue.append([linha_possivel,coluna_possivel])
        return tamanho_da_ilha
            
      for linha in range(rows):
        for coluna in range(columns):
          if grid[linha][coluna] == 1 and (linha, coluna) not in visited:
            maxArea = max(bfs(linha, coluna), maxArea)
      return maxArea
