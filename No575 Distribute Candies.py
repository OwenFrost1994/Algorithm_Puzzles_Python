# 这题表述有问题
from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        c = set(candyType)
        return min(len(candyType)//2, len(c))

solution = Solution()
print(solution.distributeCandies(candyType = [1,1,2,2,3,3]))
print(solution.distributeCandies(candyType = [1,1,2,3]))
print(solution.distributeCandies(candyType = [6,6,6,6]))
