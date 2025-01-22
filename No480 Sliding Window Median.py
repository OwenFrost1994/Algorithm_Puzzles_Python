# 随着窗口向前滑动，需要一个数据结构剔除离开窗口的数并按照顺序插入加进窗口的数, bisect包含相关功能的是insort

import bisect
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = []
        window = nums[:k]
        window.sort()
        for a, b in zip(nums, nums[k:] + [0]):
            # print([a, b])
            # print(k // 2, ~(k // 2))
            if k % 2 == 1:
                medians.append(window[k // 2] / 1.0)
            else:
                medians.append((window[k // 2] + window[k // 2 - 1]) / 2.)
            window.remove(a)
            bisect.insort(window, b)
            # medians.append((window[k // 2] + window[~(k // 2)]) / 2.)
        return medians

solution = Solution()
print(solution.medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
print(solution.medianSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 2))
print(solution.medianSlidingWindow(nums = [1,2,3,4,2,3,1,4,2], k = 3))
