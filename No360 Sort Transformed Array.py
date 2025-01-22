from typing import List

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        n = len(nums)
        index = 0 if a <= 0 else n - 1
        result = [0]*n
        i, j = 0, n - 1
        while i <= j:
            x1 = nums[i]
            x2 = nums[j]
            y1 = a * x1**2 + b * x1 + c
            y2 = a * x2**2 + b * x2 + c
            if a <= 0:
                if y1 <= y2:
                    result[index] = y1
                    i += 1
                else:
                    result[index] = y2
                    j -= 1
                index += 1
            else:
                if y1 <= y2:
                    result[index] = y2
                    j -= 1
                else:
                    result[index] = y1
                    i += 1
                index -= 1
        return result

solution = Solution()
print(solution.sortTransformedArray(nums = [-4,-2,2,4], a = 1, b = 3, c = 5))
print(solution.sortTransformedArray(nums = [-4,-2,2,4], a = -1, b = 3, c = 5))