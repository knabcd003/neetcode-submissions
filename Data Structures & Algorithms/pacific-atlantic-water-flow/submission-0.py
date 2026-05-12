class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        vectors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def inrange(r, c):
            return r >= 0 and r < len(heights) and c >= 0 and c < len(heights[0])
        def dfs(r, c, visited):
            if not inrange(r, c):
                return
            if (r, c) in visited:
                return
            visited.add((r, c))
            for x, y in vectors:
                if not inrange(r + x, c + y):
                    continue
                if heights[r + x][c + y] >= heights[r][c]:
                    dfs(r + x, c + y, visited)
        pacific = set()
        atlantic = set()
        for i in range(len(heights)):
            dfs(i, 0, pacific)
            dfs(i, len(heights[0]) - 1, atlantic)
        for i in range(len(heights[0])):
            dfs(0, i, pacific)
            dfs(len(heights) - 1, i, atlantic)
        return list(pacific & atlantic)
            