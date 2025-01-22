from typing import List
from collections import defaultdict
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        r1, c1, c2 = len(mat1), len(mat1[0]), len(mat2[0])
        result = [[0] * c2 for _ in range(r1)]
        m1 = defaultdict(set)
        m2 = defaultdict(set)
        for i in range(r1):
            for j in range(c1):
                if mat1[i][j] != 0:
                    m1[i].add(j)
        for i in range(c1):
            for j in range(c2):
                if mat2[i][j] != 0:
                    m2[j].add(i)
        for i in range(r1):
            for j in range(c2):
                indices = m1[i] & m2[j]
                for index in indices:
                    result[i][j] += mat1[i][index]*mat2[index][j]
        return result
solution = Solution()
mat1 = [[1,0,0],[-1,0,3]]
mat2 = [[7,0,0],[0,0,0],[0,0,1]]
print(solution.multiply(mat1, mat2))
mat1 = [[0]]
mat2 = [[0]]
print(solution.multiply(mat1, mat2))