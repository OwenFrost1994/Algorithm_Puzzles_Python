class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix[:] = zip(*matrix[::-1])
print(matrix)
# solution = Solution()
# print(solution.rotate(matrix))