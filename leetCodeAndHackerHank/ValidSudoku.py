# https://leetcode.com/problems/valid-sudoku/description/

def isValidSudoku(board: list[list[str]]):
  linha = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
  coluna = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
  quadrado = {(0,0):[],(0,1):[],(0,2):[],(1,0):[],(1,1):[],(1,2):[],(2,0):[],(2,1):[],(2,2):[]}
  
  for line in range(9):
    for item in range(9):
      if board[line][item] == '.':
        continue
      if board[line][item] in linha[line] or board[line][item] in coluna[item] or board[line][item] in quadrado[line//3, item//3]:
        return False
      linha[line].append(board[line][item]) 
      coluna[item].append(board[line][item])
      quadrado[line//3, item//3].append(board[line][item])
  return True
