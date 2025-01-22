from collections import deque
class Solution:
    def findMin(self, nums):
        que = deque(nums)

        while que[-1] < que[0]:
            que.appendleft(que.pop())
        
        return que[0]
    
class Solution1:
    def findMin(self, nums):
        return self.minmum(nums, 0, len(nums) - 1)
    
    def minmum(self, nums, i, j):
        if i == j:
            return nums[i]
        
        mid = (i + j) //2

        if mid == i:
            if nums[i] > nums[j]:
                return nums[j]
            else:
                return nums[i]
        
        if nums[i] >= nums[j]:
            if nums[mid] > nums[i]:
                return self.minmum(nums, mid + 1, j)
            else:
                return self.minmum(nums, i, mid)
        else:
            if nums[mid] > nums[i]:
                return self.minmum(nums, i, mid)
            else:
                return self.minmum(nums, mid + 1, j)
    
solution = Solution1()

nums = [3,1,2]
print(solution.findMin(nums))

nums = [3,4,5,1,2]
print(solution.findMin(nums))

nums = [4,5,6,7,0,1,2]
print(solution.findMin(nums))

nums = [11,13,15,17]
print(solution.findMin(nums))