class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        vectors = [(1,0), (0,1), (-1,0), (0, -1)]
        visited = set()
        def bfs(r, c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return
            if grid[r][c] != '1':
                return
            if tuple((r, c)) in visited:
                return
            visited.add((r, c))
            for u, v in vectors:
                bfs(r + u, c + v)
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and tuple((r, c)) not in visited:
                    res += 1
                    bfs(r, c)
        return res
