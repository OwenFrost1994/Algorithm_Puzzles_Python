class Solution:
    def minCostClimbingStairs(self, cost):
        if not cost:
            return 0
        dp = [0]*len(cost)
        dp[0] = cost[0]
        if len(cost) >= 2:
            dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
        return min(dp[-1], dp[-2])
        # if len(cost) == 2:
        #     return min(cost[i - 1], cost[i - 2])
        # i = len(cost)
        # totalcost1 = 0
        # while i >= 2:
        #     if cost[i - 1] < cost[i - 2]:
        #         totalcost1 = totalcost1 + cost[i - 1]
        #         i = i - 1
        #     else:
        #         totalcost1 = totalcost1 + cost[i - 2]
        #         i = i - 2
        # i = len(cost) - 1
        # totalcost2 = 0
        # while i >= 2:
        #     if cost[i - 1] < cost[i - 2]:
        #         totalcost2 = totalcost2 + cost[i - 1]
        #         i = i - 1
        #     else:
        #         totalcost2 = totalcost2 + cost[i - 2]
        #         i = i - 2
        # if totalcost1 < totalcost2:
        #     return totalcost1
        # else:
        #     return totalcost2
        
cost = [10,15,20]
solution = Solution()
print(solution.minCostClimbingStairs(cost))

cost = [1,100,1,1,1,100,1,1,100,1]
print(solution.minCostClimbingStairs(cost))

cost = [0,2,2,1]
print(solution.minCostClimbingStairs(cost))