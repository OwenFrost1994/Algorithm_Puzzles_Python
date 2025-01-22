# 0 --> 0 --> 0
# 1 --> 1 --> 1
# 2 --> 10 --> 1
# 3 --> 11 --> 2
# 4 --> 100 --> 1
# 5 --> 101 --> 2
# 6 --> 110 --> 2
# 7 --> 111 --> 3
# 8 --> 1000 --> 1
# 9 --> 1001 --> 2
# 10 --> 1010 --> 2
# 11 --> 1011 --> 3
# 12 --> 1100 --> 2
# 13 --> 1101 --> 3
# 14 --> 1110 --> 3

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        dp = [0]*(n + 1)
        dp[1] = 1
        for i in range(1, n + 1):
            if i % 2 == 0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[i//2] + 1
        return dp
    
solution = Solution()
print(solution.countBits(1))
print(solution.countBits(2))
print(solution.countBits(5))
print(solution.countBits(10))
