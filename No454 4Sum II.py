from collections import Counter
from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter = Counter()
        for a in nums1:
            for b in nums2:
                counter[a + b] += 1
        ans = 0
        for c in nums3:
            for d in nums4:
                # adding for every time -(c+d)
                ans += counter[-(c + d)]
        return ans

solution = Solution()
print(solution.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))
print(solution.fourSumCount(nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]))