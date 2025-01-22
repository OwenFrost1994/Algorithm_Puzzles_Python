from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1
        return [i + 1 for i, v in enumerate(nums) if v > 0]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        result =[]
        i = 0
        n = len(nums)
        nums.append(n + 1)
        nums = [0] + nums
        while i < n + 1:
            while i < n + 1 and nums[i + 1] == nums[i]:
                i += 1
            a = 1
            while i < n + 1 and nums[i + 1] > nums[i] + a:
                result.append(nums[i] + a)
                a += 1
            i += 1
        return result
    
solution = Solution()
print(solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(solution.findDisappearedNumbers([1,1]))
print(solution.findDisappearedNumbers([1,1,1]))
print(solution.findDisappearedNumbers([2,2]))