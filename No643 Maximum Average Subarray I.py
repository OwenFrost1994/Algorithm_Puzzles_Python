from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        suma = sum(nums[:k])
        maxave = suma/k
        for i in range(1, len(nums) - k + 1):
            suma = suma - nums[i-1] + nums[i-1+k]
            maxave = max(maxave, suma/k)
        return maxave

solution = Solution()
print(solution.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4))
print(solution.findMaxAverage(nums = [5], k = 1))
print(solution.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 3))