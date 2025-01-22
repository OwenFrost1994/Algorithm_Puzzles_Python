class Solution:
    def combine(self, n, k):
        nums = list(range(1, n + 1))
        result = []
        results = []
        self.combination(result, nums, 0, k, results)
        return results

    def combination(self, result, nums, index, k, results):
        if k == 0:
            results.append(result.copy())
            return
        if index == len(nums):
            return
        for i in range(index, len(nums)):
            result.append(nums[i])
            self.combination(result, nums, i + 1, k - 1, results)
            result.pop()
        
n = 4
k = 3
solution = Solution()
print(solution.combine(n, k))

n = 1
k = 1
print(solution.combine(n, k))