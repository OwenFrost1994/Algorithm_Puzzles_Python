class Solution:
    def maxProfit(self, prices):
        return self.dfs(prices, 0, 0, 0)
    
    def dfs(self, prices, index, profit, operation):
        if index == len(prices) - 1 or operation == 2:
            return 0
        newprofit = 0
        for i in range(index, len(prices) - 1):
            for j in range(i + 1, len(prices)):
                if prices[j] > prices[i]:
                    newprofit = max(newprofit, prices[j] - prices[i] + self.dfs(prices, j + 1, 0, operation + 1))
                else:
                    continue
        return profit + newprofit

class Solution1:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        dp = [[0]*len(prices) for _ in range(3)]

        for k in range(1, 3):
            for i in range(len(prices)):
                minmal = prices[0]
                for j in range(1, i+1):
                    minmal = min(minmal, prices[j] - dp[k-1][j-1])  
                    dp[k][i] = max(dp[k][i-1], prices[i] - minmal)

        return dp[2][len(prices) - 1]

solution = Solution1()

prices = [3,3,5,0,0,3,1,4]
print(solution.maxProfit(prices))

prices = [1,2,3,4,5]
print(solution.maxProfit(prices))

prices = [7,6,4,3,1]
print(solution.maxProfit(prices))