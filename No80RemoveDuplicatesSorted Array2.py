class Solution:
    def removeDuplicates(self, nums):
        index1 = 1
        index2 = 0
        repeat = 1
        k = 1
        while(index1 < len(nums)):
            if nums[index1] == nums[index2] and repeat < 2:
                index2 += 1
                nums[index2] = nums[index1]
                index1 += 1
                repeat += 1
                k += 1
                continue
            if nums[index1] == nums[index2] and repeat == 2:
                while(index1 < len(nums) and nums[index1] == nums[index2]):
                    index1 += 1
                repeat == 0
                continue
            if nums[index1] != nums[index2]:
                index2 += 1
                nums[index2] = nums[index1]
                index1 += 1
                repeat = 1
                k += 1
        return k
    
nums = [1,1,1,2,2,3]
solution = Solution()
# print(solution.removeDuplicates(nums))

nums = [0,0,1,1,1,1,2,3,3]
print(solution.removeDuplicates(nums))