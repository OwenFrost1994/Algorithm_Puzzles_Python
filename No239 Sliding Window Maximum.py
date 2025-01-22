class Solution:
    def maxSlidingWindow(self, nums, k):
        result = []
        for i in range(len(nums) - k + 1):
            result.append(max(nums[i: i + k]))
        return result
    
from collections import deque
class Solution1:
    def maxSlidingWindow(self, nums, k):
        result = []
        window = deque()

        for i, num in enumerate(nums):
            while window and window[0] < i - k + 1:
                window.popleft()

            while window and nums[window[-1]] < num:
                window.pop()

            window.append(i)

            if i >= k - 1:
                result.append(nums[window[0]])

        return result

solution = Solution1()

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(solution.maxSlidingWindow(nums, k))

nums = [1]
k = 1
print(solution.maxSlidingWindow(nums, k))