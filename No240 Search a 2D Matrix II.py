class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        r = 0
        c = column - 1
        while r < row and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False
    
solution = Solution()
matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(solution.searchMatrix(matrix, target))

matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
print(solution.searchMatrix(matrix, target))