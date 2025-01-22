class Solution:
    def wiggleSort(self, nums) -> None:
        nums.sort()
        mid = (len(nums) - 1)//2
        nums[::2], nums[1::2] = nums[mid::-1], nums[len(nums):mid:-1]
        """
        Do not return anything, modify nums in-place instead.
        """
solution = Solution()
print(solution.wiggleSort([1,5,1,1,6,4]))
print(solution.wiggleSort([1,3,2,2,3,1]))