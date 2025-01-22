class Solution(object):
    def perfunction(self, result, nums, index):
        if index == len(nums):
            result.append(nums[:])
            return
        for i in range(index, len(nums)):
            nums[i],nums[index] = nums[index],nums[i]
            self.perfunction(result, nums, index + 1)
            nums[i],nums[index] = nums[index],nums[i]

    def permute(self, nums):
        result = []
        self.perfunction(result, nums[:], 0)
        return result

nums = [1,2,3]

solution = Solution()
print(solution.permute(nums))