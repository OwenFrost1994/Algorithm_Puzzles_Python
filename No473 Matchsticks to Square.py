# 一个dfs类问题,或者说依次把每一个棍填充进一个4*[0]的array里面保证array最终数字一样
# 要从小到大排序，从大到小，每一次填充一个matchsticks的要素,沿着matchsticks一次深入,如果高度一样就往后面填充
# 边缘条件是如果sticks总长度不能整除或者除的长度比最长的还短那就不行
# 做题做多了其实应该自己写一下过程,思考一下自己用啥方法改进而不是瞎猜

from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def dfs(index):
            if index == len(matchsticks):
                return True
            for i in range(4):
                if i > 0 and edges[i - 1] == edges[i]:
                    continue
                edges[i] += matchsticks[index]
                if edges[i] <= edge and dfs(index + 1):
                    return True
                edges[i] -= matchsticks[index]
            return False
        
        edge, resi = divmod(sum(matchsticks), 4)
        if resi != 0 or edge < max(matchsticks):
            return False
        edges = [0]*4
        matchsticks.sort(reverse = True)
        return dfs(0)

solution = Solution()
print(solution.makesquare([1,1,2,2,2]))
print(solution.makesquare([3,3,3,3,4]))
