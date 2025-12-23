# https://leetcode.com/problems/number-of-islands/
# 200. Number of Islands

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int: 
      grupo_num = 0
      rows, cols = len(grid), len(grid[0])
      visited = set()  
        
      def bfs(linha, coluna):
        linhaAdj, colunaAdj = linha, coluna
        dirs = [[0,-1],[-1,0],[0,1],[1,0]] # esquerda, cima, direita, baixo
        processing = [[linha,coluna]] # locais para processar
        while processing:
          blocoProcessando = processing.pop(0)
          linha, coluna = blocoProcessando[0], blocoProcessando[1]
          for dir_ in dirs:
            linhaAdj = linha + dir_[0]
            colunaAdj = coluna + dir_[1]
            if linhaAdj not in range(rows) or colunaAdj not in range(cols) or grid[linhaAdj][colunaAdj] == "0" or (linhaAdj, colunaAdj) in visited: continue  
            # já coloco ele no grupo dele
            visited.add((linhaAdj, colunaAdj))        # isso serve como uma marcacao como visitado também!     
            processing.append([linhaAdj,colunaAdj]) # depois vou processar os adjascentes a ele

      for line in range(rows):
        for column in range(cols):
          if grid[line][column] == "1" and (line, column) not in visited:
            grupo_num += 1
            bfs(line, column)
      return grupo_num
