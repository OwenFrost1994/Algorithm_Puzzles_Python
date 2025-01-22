import collections
class Solution(object):
    def rotate(self, nums, k):
        if len(nums) <= 1 or k == 0:
            return nums
        k = k % len(nums)
        if k == 0:
            return nums
        nums = collections.deque(nums)
        for i in range(k):
            nums.appendleft(nums.pop())
        newnums = []
        while(len(nums)>0):
            newnums.append(nums.popleft())
        return newnums

nums = [1,2,3,4,5,6,7]
k = 3
solution = Solution()
print(solution.rotate(nums, k))

nums = [-1,-100,3,99]
k = 2
print(solution.rotate(nums, k))