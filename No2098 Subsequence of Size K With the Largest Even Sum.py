from typing import List

class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        result = sum(nums[:k])
        if result % 2 == 0:
            return result
        min_odd = float("inf")
        min_eve = float("inf")
        for i in range(k):
            if nums[i] % 2 == 0:
                min_eve = min(min_eve, nums[i])
            else:
                min_odd = min(min_odd, nums[i])
        ans = -1
        for i in range(k, n):
            if nums[i] % 2 and min_eve != 10 ** 6:
                ans = max(ans, result - min_eve + nums[i])
            if nums[i] % 2 == 0 and min_odd != 10 ** 6:
                ans = max(ans, result - min_odd + nums[i])
        
        return ans
solution = Solution()
print(solution.largestEvenSum(nums = [4,1,5,3,1], k = 3))
print(solution.largestEvenSum(nums = [4,6,2], k = 3))
print(solution.largestEvenSum(nums = [1,3,5], k = 1))