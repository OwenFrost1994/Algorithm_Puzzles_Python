class Solution:
    def thirdMax(self, nums) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)
        if len(nums) < 3:
            return nums[0]
        return nums[2]

solution = Solution()
nums = [3,2,1]
print(solution.thirdMax(nums))
nums = [1,2]
print(solution.thirdMax(nums))
nums = [2,2,3,1]
print(solution.thirdMax(nums))