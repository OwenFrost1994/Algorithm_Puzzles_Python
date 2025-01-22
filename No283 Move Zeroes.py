class Solution:
    def moveZeroes(self, nums) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
            if nums[slow] != 0:
                slow += 1

solution = Solution()

nums = [0,1,0,3,12]
print(solution.moveZeroes(nums))

nums = [0]
print(solution.moveZeroes(nums))