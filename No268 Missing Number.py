class Solution(object):
    def missingNumber(self, nums):
        nums.sort()

        if nums[0] != 0:
            return 0
        for i in range(len(nums) - 1):
            if nums[i + 1] != nums[i] + 1:
                return nums[i] + 1
        return len(nums)

solution = Solution()

nums = [3,0,1]
print(solution.missingNumber(nums))

nums = [0,1]
print(solution.missingNumber(nums))

nums = [9,6,4,2,3,5,7,0,1]
print(solution.missingNumber(nums))