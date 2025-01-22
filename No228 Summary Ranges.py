class Solution:
    def summaryRanges(self, nums):
        result = []
        left = 0
        right = 0
        while right < len(nums):
            if right < len(nums) - 1 and nums[right] + 1 == nums[right + 1]:
                    right += 1
            else:
                if right == left:
                    result.append(str(nums[left]))
                else:
                    result.append(str(nums[left]) + "->" + str(nums[right]))
                right = right + 1
                left = right
        return result
    
solution = Solution()
nums = [0,1,2,4,5,7]
print(solution.summaryRanges(nums))

nums = [0,2,3,4,6,8,9]
print(solution.summaryRanges(nums))