class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        row = -1
        while l <= r:
            mid = (l + r) // 2
            if matrix[mid][0] <= target and target <= matrix[mid][len(matrix[mid]) - 1]:
                #found our row
                row = mid
                break
            elif matrix[mid][len(matrix[mid]) - 1] < target:
                l = mid + 1
            else:
                r = mid - 1
        if row == -1:
            return False
        l = 0
        r = len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                #found target
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False