"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}
        def dfs(n):
            if not n:
                return
            if n not in cloned:
                cloned[n] = Node(n.val, [])
            else:
                return
            for neighbor in n.neighbors:
                dfs(neighbor)
                cloned[n].neighbors.append(cloned[neighbor])
        dfs(node)
        return cloned.get(node, None)


