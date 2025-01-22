class Solution:
    results = []
    def subsetsWithDup(self, nums):
        self.results = []
        nums.sort()
        for i in range(0, len(nums) + 1):
            result = []
            self.subsetgener(nums, result, 0, i)
        return self.results
    
    def subsetgener(self, nums, result, index, length):
        if len(result) == length:
            if result not in self.results:
                self.results.append(result.copy())
            return
        for i in range(index, len(nums)):
            result.append(nums[i])
            self.subsetgener(nums, result, i + 1, length)
            result.pop()

solution = Solution()

nums = [1,2,2]
print(solution.subsetsWithDup(nums))

nums = [0]
print(solution.subsetsWithDup(nums))

nums = [4,4,4,1,4]
print(solution.subsetsWithDup(nums))