class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        if nums == None or len(nums) == 0 or sum(nums) < target:
            return 0
        i=0
        j=0
        numsum=0
        minlen = len(nums)
        while j < len(nums):
            numsum += nums[j]
            j += 1
            while numsum >= target:
                minlen = min(j - i, minlen)
                numsum -= nums[i]
                i += 1
        return minlen

solution = Solution()

target = 7
nums = [2,3,1,2,4,3]
print(solution.minSubArrayLen(target, nums))

target = 4
nums = [1,4,4]
print(solution.minSubArrayLen(target, nums))

target = 11
nums = [1,1,1,1,1,1,1,1]
print(solution.minSubArrayLen(target, nums))