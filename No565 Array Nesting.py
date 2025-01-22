from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans, n = 0, len(nums)
        for i in range(n):
            cnt = 0
            while nums[i] != n:
                j = nums[i]
                nums[i] = n
                i = j
                cnt += 1
            ans = max(ans, cnt)
        return ans

solution = Solution()
print(solution.arrayNesting(nums = [0,1,2]))
print(solution.arrayNesting(nums = [5,4,0,3,1,6,2]))