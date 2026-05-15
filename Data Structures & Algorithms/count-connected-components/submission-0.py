class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)

        res = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        return res
                