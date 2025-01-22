from collections import Counter
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        ans = 0
        for p in points:
            counter = Counter()
            for q in points:
                distance = (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1])
                counter[distance] += 1
            ans += sum([val * (val - 1) for val in counter.values()])
        return ans

solution = Solution()
print(solution.numberOfBoomerangs(points = [[0,0],[1,0],[2,0]]))
print(solution.numberOfBoomerangs(points = [[1,1],[2,2],[3,3]]))
print(solution.numberOfBoomerangs(points = [[1,1]]))