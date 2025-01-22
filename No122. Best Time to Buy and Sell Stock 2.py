class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit
    
solution = Solution()

prices = [7,1,5,3,6,4]
print(solution.maxProfit(prices))

prices = [1,2,3,4,5]
print(solution.maxProfit(prices))

prices = [7,6,4,3,1]
print(solution.maxProfit(prices))