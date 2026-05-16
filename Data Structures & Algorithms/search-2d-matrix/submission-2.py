class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW, COL = len(matrix), len(matrix[0])
        i, j = 0,0
        result = 0
        while i < ROW:
            if j+1 < COL and matrix[i][j + 1] <= target:
                j += 1
                continue
            result = matrix[i][j]
            if matrix[i][j] == target:
                return True
            i += 1
            j = 0
        return False