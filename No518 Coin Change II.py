# "无界背包问题"：可以无限次拾取物品
# dp[i] += dp[i - coin]这个地方+必须得有
from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]

solution = Solution()
print(solution.change(amount = 3, coins = [2]))
print(solution.change(amount = 10, coins = [10]))
print(solution.change(amount = 5, coins = [1,2,5]))