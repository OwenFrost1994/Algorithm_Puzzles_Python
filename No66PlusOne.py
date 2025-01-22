class Solution(object):
    def plusOne(self, digits):
        nums = [0]
        nums.extend(digits)

        isten = 0
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                nums[i] = nums[i] + 1
            nums[i] = nums[i] + isten
            if nums[i] >= 10:
                nums[i] = nums[i] % 10
                isten = 1
            else:
                isten = 0
        if nums[0] == 0:
            return nums[1:len(nums)]
        else:
            return nums
        
digits = [1,2,3]
solution = Solution()
print(solution.plusOne(digits))

digits = [4,3,2,1]
print(solution.plusOne(digits))

digits = [9]
print(solution.plusOne(digits))