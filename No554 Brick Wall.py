# 因为边缘不算，实际上就看砖的右侧位置是哪里，右侧位置最多的那个地方穿过的最少

from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        right = defaultdict(int)
        for w in wall:
            width = 0
            for brick in w[:-1]:
                width += brick
                right[width] += 1
        if not right:
            return len(wall)
        return len(wall) - right[max(right, key = right.get)]

solution = Solution()
print(solution.leastBricks(wall = [[1],[1],[1]]))
print(solution.leastBricks(wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]))