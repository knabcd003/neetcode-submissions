class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix = [[0] * len(matrix[0]) for i in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                self.prefix[row][col] = matrix[row][col]
                if row > 0 and col > 0:
                    self.prefix[row][col] += (self.prefix[row - 1][col] + self.prefix[row][col - 1] - self.prefix[row - 1][col - 1])
                elif row > 0:
                    self.prefix[row][col] += self.prefix[row - 1][col]
                elif col > 0:
                    self.prefix[row][col] += self.prefix[row][col - 1]
                        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bigSquare = self.prefix[row2][col2]
        if row1 > 0 and col1 > 0:
            bigSquare -= (self.prefix[row1 - 1][col2] + self.prefix[row2][col1 - 1] - self.prefix[row1 -  1][col1 - 1])
        elif row1 > 0:
            bigSquare -= self.prefix[row1 - 1][col2]
        elif col1 > 0:
            bigSquare -= self.prefix[row2][col1 - 1]
        return bigSquare

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)