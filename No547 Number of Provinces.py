# A dfs of grah
# isConnected is indeed symmetric
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            isvisited[i] = True
            for j, val in enumerate(isConnected[i]):
                if not isvisited[j] and val == 1:
                    dfs(j)

        n = len(isConnected)
        isvisited = [False] * n
        result = 0
        for i in range(n):
            if not isvisited[i]:
                dfs(i)
                result += 1
        return result

solution = Solution()
print(solution.findCircleNum(isConnected = [[1,1,0],[1,1,0],[0,0,1]]))
print(solution.findCircleNum(isConnected = [[1,0,0],[0,1,0],[0,0,1]]))