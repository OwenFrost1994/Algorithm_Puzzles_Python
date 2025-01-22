from itertools import accumulate
from typing import List

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0]*length
        for l, r, v in updates:
            nums[l] += v
            if r + 1 < length:
                nums[r + 1] -= v
        return list(accumulate(nums))
    
class Solution1:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        nums = [0]*length
        for l, r, v in updates:
            nums[l] += v
            if r + 1 < length:
                nums[r + 1] -= v
        val = 0
        for i in range(length):
            val = val + nums[i]
            nums[i] = val
        return nums

solution = Solution1()
print(solution.getModifiedArray(length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]))
print(solution.getModifiedArray(length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]))