class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        def isValid(node, prev, visited):
            if node in visited:
                return False
            print("level:", node)
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor != prev:
                    if not isValid(neighbor, node, visited):
                        return False
            return True
        visit = set()
        return isValid(0, -1, visit) and len(visit) == n