class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()

        maxlen = 0
        for i in range(len(nums) - 1):
            maxlen = max(maxlen, abs(nums[i + 1] - nums[i]))
        return maxlen
    
solution = Solution()

nums = [3,6,9,1]
print(solution.maximumGap(nums))

nums = nums = [10]
print(solution.maximumGap(nums))
