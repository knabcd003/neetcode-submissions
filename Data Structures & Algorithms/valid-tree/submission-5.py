class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
        
        visited = set()
        def isValid(node, prev):
            if node in visited:
                return False
            print("level:", node)
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor != prev:
                    if not isValid(neighbor, node):
                        return False
            return True
        visit = set()
        return isValid(0, -1) and len(visited) == n