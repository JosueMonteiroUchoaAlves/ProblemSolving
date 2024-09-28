# https://leetcode.com/problems/course-schedule-ii/description/
# 210. Course Schedule II

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
      courses  = { i:[] for i in range(numCourses)}
      visiting = set()
      visited = set()
      answer = []
      
      for crs, pre in prerequisites:
        courses[crs].append(pre)

      def dfs(n):
        if n in visited:
          return True
        if n in visiting:
          return False
        
        visiting.add(n)
        
        for adj in courses[n]:
          if not dfs(adj): return False
        visiting.remove(n)
        visited.add(n)
        answer.append(n)
        return True
      for crs in courses:
        if not dfs(crs): return []
      return answer
