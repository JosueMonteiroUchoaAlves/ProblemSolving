# https://leetcode.com/problems/course-schedule/description/
# 207. Course Schedule

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
  edges = {i:[] for i in range(numCourses)}
  visiting = set()
  
  for crs, pre in prerequisites:
    edges[crs].append(pre)
     
  def bfs(crs):
    if edges[crs] == []:
      return True
    if crs in visiting:
      return False
    visiting.add(crs)
    
    for parent in edges[crs]:
      if not bfs(parent): return False # se tiver um loop em algum parente ja nn vai ser possivel
      
    visiting.remove(crs) #ja vi se ele e possivel
    edges[crs] = [] # se todos os parentes dele sao possiveis, posso tiralos
    return True

  for course in edges:
    if not bfs(course): return False
  return True
print(canFinish(2, [[1,0],[0,1]]))
