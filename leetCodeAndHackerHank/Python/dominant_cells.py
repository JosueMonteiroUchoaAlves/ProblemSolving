
def check_neighbors(grid, co, ro):
  item = grid[ro][co]
  
  neighbors = [
    [-1, -1], [-1, 0],[-1, 1],
    [0, -1],           [0, 1],
    [1, -1],  [1, 0],  [1, 1]
    ]
  for nei in neighbors:
    r, c = ro + nei[0], co + nei[1] # row and column of this neighbor
    if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]):
      continue
    if grid[r][c] < item:
      continue
    else:
      break
  else:
    return True
  return False

def numCells(grid):
  for row in range(len(grid)):
    grid[row] = list(map(int, grid[row]))
  print(type(grid[0][0]))
  assert len(grid) in range(1, 501) and len(grid[0]) in range(1, 501)
  total_dominant_cells = 0
  for row in range(len(grid)):
    for column in range(len(grid[row])):
      if check_neighbors(grid,column, row):
        total_dominant_cells += 1
  return total_dominant_cells

grid = [["1"," 2", "7"], ["4", 5, 6], [8, 8 ,9]]
print(numCells(grid))
