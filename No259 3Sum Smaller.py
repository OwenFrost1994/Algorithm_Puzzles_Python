class Solution:
    def threeSumSmaller(self, nums, target: int) -> int:
        n = len(nums)
        results = 0
        nums.sort()
        if n < 3:
            return 0
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                numsum = nums[i] + nums[j] + nums[k]
                if numsum >= target:
                    k -= 1
                else:
                    results += k - j
                    j += 1
        return results

solution = Solution()
print(solution.threeSumSmaller(nums = [-2,0,1,3], target = 2))
print(solution.threeSumSmaller(nums = [], target = 0))
print(solution.threeSumSmaller(nums = [0], target = 0))