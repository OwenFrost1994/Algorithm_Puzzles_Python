class Solution:
    def threenumbers(self, nums):
        result = nums.copy()
        for i in range(3):
            for j in range(3):
                if i != j:
                    result.append(10*nums[i]+nums[j])
        return result[nums[2]-1]

solution = Solution()
print(solution.threenumbers([1,4,8]))