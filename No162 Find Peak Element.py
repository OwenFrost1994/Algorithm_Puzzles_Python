class Solution:
    def findPeakElement(self, nums):
        if len(nums) == 1:
          return 0
        
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = start + ((end - start)//2)
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid  + 1
        return start


solution = Solution()

nums = [1,2,3,1]
print(solution.findPeakElement(nums))

nums = [1,2,1,3,5,6,4]
print(solution.findPeakElement(nums))