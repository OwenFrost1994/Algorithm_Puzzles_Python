class Solution:
    def wiggleSort(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        n = len(nums)
        mid = (n - 1)//2
        nums[::2], nums[1::2] = nums[mid::-1], nums[n:mid:-1]
        return
solution = Solution()
nums = [3,5,2,1,6,4]
solution.wiggleSort(nums)
print(nums)
nums = [6,6,5,6,3,8]
solution.wiggleSort(nums)
print(nums)
nums = [3,5,2,6,4]
solution.wiggleSort(nums)
print(nums)