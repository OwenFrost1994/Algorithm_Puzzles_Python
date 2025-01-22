from collections import defaultdict
from typing import List

class Solution:
    def MLS(self , arr: List[int]) -> int:
        # write code here
        # 我有两个办法，一个排序加双指针，一个用hash map可以到O(n)，我用第一个试试
        # mp[num] = [left, right]
        mp = defaultdict(list)
        maxl = 1
        for nums in arr:
            if nums not in mp.keys():
                left, right = nums, nums
                if nums - 1 in mp.keys():
                    left = mp[nums - 1][0]
                if nums + 1 in mp.keys():
                    right = mp[nums + 1][1]
                mp[right] = [left, right]
                mp[left] = [left, right]
                mp[nums] = [left, right]
                maxl = max(maxl, right - left + 1)
        return maxl

solution = Solution()
print(solution.MLS([100,4,200,1,3,2]))