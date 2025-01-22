# (x + 1)*x/2 <= n
# x^2 + x + 1/4 <= 2n + 1/4
# -sqrt(2n + 1/4) <= x + 1/2 <= sqrt(2n + 1/4)
# -sqrt(2n + 1/4) - 1/2 <= x <= sqrt(2n + 1/4) - 1/2
# -sqrt(2n + 1/4) - 1/2 <= x <= sqrt(8n + 1)/2 - 1/2

import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(math.sqrt(8*n + 1)/2 - 0.5)

solution = Solution()
print(solution.arrangeCoins(5))
print(solution.arrangeCoins(8))
