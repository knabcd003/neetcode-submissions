class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        sqr = [[set() for i in range(3)] for _ in range(3)]
        for r, row in enumerate(board):
            for c, col in enumerate(row):
                if col in rows[r] or col in cols[c]:
                    print(rows[r], rows[c], col)
                    return False
                if col in sqr[r//3][c//3]:
                    return False
                if col != ".":
                    rows[r].add(col)
                    cols[c].add(col)
                    sqr[r//3][c//3].add(col)
        return True