from math import sqrt
from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(sqrt(area))
        while area % w != 0:
            w -= 1
        return [area//w, w]

solution = Solution()
print(solution.constructRectangle(area = 4))
print(solution.constructRectangle(area = 37))
print(solution.constructRectangle(area = 122122))