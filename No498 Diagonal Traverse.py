# 一共是走m+n个对角线，这个别忘了，对角线有反序，靠模来判断
# 总共的对角线数量是m+n-1
# 离谱的是他很多矩阵不是方的，这个小心
from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        results = []
        for k in range(m + n - 1):
            temp = []
            if k < n:
                nn = k + 1
                x = 0
                y = k
            else:
                nn = m + n - 1 - k
                x = k - n + 1
                y = n - 1
            while x < m and y >= 0:
                temp.append(mat[x][y])
                x += 1
                y -= 1
            if k % 2 == 0:
                temp.reverse()
            results.extend(temp)
        return results
    
solution = Solution()
print(solution.findDiagonalOrder(mat = [[2,3]]))
print(solution.findDiagonalOrder(mat = [[1,2],[3,4]]))
print(solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(solution.findDiagonalOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
print(solution.findDiagonalOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]))