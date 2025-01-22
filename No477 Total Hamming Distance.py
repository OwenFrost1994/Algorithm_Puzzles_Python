from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        maxnum = max(nums)
        digit = 0
        while maxnum != 0:
            digit += 1
            maxnum = maxnum // 2
        result = 0
        for i in range(digit + 1):
            a, b = 0, 0
            for num in nums:
                isone = (num >> i) & 1
                if isone:
                    a += 1
                else:
                    b += 1
            result += a * b
        return result

solution = Solution()
print(solution.totalHammingDistance([1337,7331]))
print(solution.totalHammingDistance([4,14,2]))
print(solution.totalHammingDistance([4,14,4]))