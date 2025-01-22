from math import floor, sqrt
from functools import lru_cache
@lru_cache(None)
def dp(n):
    if n == 0:
        return 0
    nums = []
    for i in range(floor(sqrt(n))):
        nums.append(dp(n - (i + 1)**2))
    return min(nums) + 1
class Solution:
    def numSquares(self, n: int) -> int:
        return dp(n)
def dp1(n):
    return 0 if n == 0 else min(dp(n-(x+1)**2) for x in range(floor(sqrt(n)))) + 1
solution = Solution()
print(solution.numSquares(12))
print(solution.numSquares(13))