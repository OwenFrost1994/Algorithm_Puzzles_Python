# 单调堆栈找一个值后面的最接近的大值

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        stk = []
        for v in nums2:
            while stk and stk[-1] < v:
                m[stk.pop()] = v
            stk.append(v)
        return [m.get(v, -1) for v in nums1]


solution = Solution()
print(solution.nextGreaterElement(nums1 = [4,1,2], nums2 = [1,3,4,2]))
print(solution.nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4]))
