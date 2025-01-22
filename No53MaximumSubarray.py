class Solution:
    def maxSubArray(self, nums):
        # @cache
        def solve(i, must_pick):
            if i >= len(nums): return 0 if must_pick else float('-inf')
            return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
        return solve(0, False)

solution = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(solution.maxSubArray(nums))