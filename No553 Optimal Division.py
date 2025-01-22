from typing import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return str(nums[0])
        if n == 2:
            return f'{nums[0]}/{nums[1]}'
        return f'{nums[0]}/({"/".join(map(str, nums[1:]))})'

solution = Solution()
print(solution.optimalDivision(nums = [1000,100,10,2]))
print(solution.optimalDivision(nums = [2,3,4]))