class Solution:
    results = []
    def subsets(self, nums):
        self.results = []
        for i in range(0, len(nums) + 1):
            result = []
            self.subsetgener(nums, result, 0, i)
        return self.results
    
    def subsetgener(self, nums, result, index, length):
        if len(result) == length:
            self.results.append(result.copy())
            return
        for i in range(index, len(nums)):
            result.append(nums[i])
            self.subsetgener(nums, result, i + 1, length)
            result.pop()

solution = Solution()

nums = [1,2,3]
print(solution.subsets(nums))

nums = [0]
print(solution.subsets(nums))