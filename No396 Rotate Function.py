# F(k) = 0 * arrk[0] + 1 * arrk[1] + ... + (n - 1) * arrk[n - 1].
# for [A, B, C, D]
# F(0) = 0A + 1B + 2C + 3D
# F(1) = 0D + 1A + 2B + 3C (= F(0) + (A + B + C + D) - nD)
# F(2) = 0C + 1D + 2A + 3B (= F(1) + (A + B + C + D) - nC)
# F(3) = 0B + 1C + 2D + 3A (= F(2) + (A + B + C + D) - nD)

from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total = sum(nums)
        n = len(nums)
        result = sum([nums[i]*i for i in range(n)])
        F1 = result
        for i in range(1, n):
            F1 = F1 + total - n*nums[n - i]
            result = max(result, F1)
        return result

solution = Solution()
print(solution.maxRotateFunction([4,3,2,6]))
print(solution.maxRotateFunction([100]))