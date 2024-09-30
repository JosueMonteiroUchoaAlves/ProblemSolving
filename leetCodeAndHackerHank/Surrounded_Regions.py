# https://leetcode.com/problems/surrounded-regions/submissions/1404269557/
# 130. Surrounded Regions
def solve(board: list[list[str]]) -> None:
  linhas, colunas = len(board), len(board[0])
  deque = []
  visited = set()
  
  def bfs(l, c):
    deque.append([l, c])
    directions = [[1,0],[0,1],[-1,0],[0,-1]] # direita, baixo, esquerda, cima
    while deque:
      atual = deque.pop(0)
      l, c = atual
      board[l][c] = "STAY"
      for direction in directions:
        adj_l, adj_c = l + direction[0], c + direction[1]
        if adj_l not in range(linhas) or adj_c not in range(colunas) or board[adj_l][adj_c] == "X" or (adj_l, adj_c) in visited: continue
        visited.add((adj_l,adj_c))
        deque.append([adj_l, adj_c])
        
    return
  for l in range(linhas):
    if board[l][0] == "O" and (l, 0) not in visited:
      bfs(l, 0)
    if board[l][colunas-1] == "O" and (l, colunas-1) not in visited:
      bfs(l, colunas-1)
    
  for c in range(colunas):
    if board[0][c] == "O" and (0, c) not in visited:
      bfs(0, c)
    if board[linhas-1][c] == "O" and (linhas-1, c) not in visited:
      bfs(linhas-1, c)

  for line in range(linhas):
    for column in range(colunas):
      if board[line][column] != "STAY":
        board[line][column] = "X"
      else:
        board[line][column] = "O"

print(solve([["X"]]))
