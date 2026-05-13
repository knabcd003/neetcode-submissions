class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for x, y in prerequisites:
                adj[x].append(y)
        
        def dfs(course, visited):
            if course in visited:
                return False
            visited.add(course)
            for neighbor in adj[course]:
                if not dfs(neighbor, visited):
                  return False
            visited.remove(course)
            return True

        for c in range(numCourses):
            visit = set()
            canFinis = dfs(c, visit)
            if not canFinis:
                return False
        return True


