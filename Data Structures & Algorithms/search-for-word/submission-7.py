class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def backtrack(r, c, i, visited):
            if i == len(word):
                return True
            if r >= len(board) or r < 0 or c < 0 or c >= len(board[0]):
                return False
            if board[r][c] != word[i]:
                return False
            if tuple((r, c)) in visited:
                return False
            visited.add(tuple((r, c)))
            i += 1
            for a, b in vectors:
                if backtrack(r + a, c + b, i, visited):
                    return True
            visited.remove(tuple((r, c)))
            i -= 1
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if backtrack(i, j, 0, set()):
                    return True
        return False
            

            
            
            

            
            