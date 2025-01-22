# a large number can be divided by a small number then the larger one is the parent of smaller one
# for a < b < c in nums, if b % a == 0 and c % b == 0, then we must have c % a == 0
# what we need to do is find a's parent b and b's parent c
# then we know the length of set by in creasing the set that %b is zero by 1
# dp[i] record the length of set that involves nums[i], parent[i] record the parent of nums[i]
# the transversal must go from large to small
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [0] * n
        parent = [0] * n
        maxlen = 0
        setindex = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n): # cannot be i + 1 some times i = n - 1
                if nums[j] % nums[i] == 0 and dp[i] < dp[j] + 1: # ensure the contemporary length of set nums[i] in is not longer than the new one
                    dp[i] = dp[j] + 1
                    parent[i] = j
                    if dp[i] > maxlen:# record the maximum length and the index of head number of set
                        maxlen = dp[i]
                        setindex = i
        result = []
        for i in range(maxlen):
            result.append(nums[setindex])
            setindex = parent[setindex]
        return result

solution = Solution()
print(solution.largestDivisibleSubset(nums = [1,2,3]))
print(solution.largestDivisibleSubset(nums = [1,2,4,8]))