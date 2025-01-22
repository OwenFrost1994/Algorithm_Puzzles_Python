# 松鼠只能一次拿一个,如果从树上开始,那就是总距离乘2
# 不从树上开始，从其中一个开始，那就得看树到nut的距离，和nut到松鼠的距离，需要减去一个nut到树的距离加上一个nut到松鼠的开始距离
from math import inf
from typing import List

class Solution:
    def minDistance(
        self,
        height: int,
        width: int,
        tree: List[int],
        squirrel: List[int],
        nuts: List[List[int]],
    ) -> int:
        x, y, a, b = *tree, *squirrel
        s = sum(abs(i - x) + abs(j - y) for i, j in nuts) * 2
        result = inf
        for i, j in nuts:
            c = abs(i - x) + abs(j - y)
            d = abs(i - a) + abs(j - b)
            result = min(result, s - c + d)
        return result

solution = Solution()
print(solution.minDistance(height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0], [2,5]]))
print(solution.minDistance(height = 1, width = 3, tree = [0,1], squirrel = [0,0], nuts = [[0,2]]))