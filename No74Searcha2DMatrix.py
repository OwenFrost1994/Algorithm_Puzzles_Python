class Solution(object):
    def searchMatrix(self, matrix, target):
        if target > matrix[len(matrix) - 1][len(matrix[len(matrix) - 1]) - 1] or target < matrix[0][0]:
            return False
        for i in range(len(matrix)):
            if target == matrix[i][0] or target == matrix[i][len(matrix[i]) - 1]:
                return True
            if target > matrix[i][0] and target < matrix[i][len(matrix[i]) - 1]:
                left = 0
                right = len(matrix[i]) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        left = mid + 1
                    else:
                        right = mid - 1
                break
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
solution = Solution()
print(solution.searchMatrix(matrix, target))

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(solution.searchMatrix(matrix, target))

matrix = [[1]]
target = 1
print(solution.searchMatrix(matrix, target))

matrix = [[-8,-7,-5,-3,-3,-1,1],[2,2,2,3,3,5,7],[8,9,11,11,13,15,17],[18,18,18,20,20,20,21],[23,24,26,26,26,27,27],[28,29,29,30,32,32,34]]
target = -5
print(solution.searchMatrix(matrix, target))