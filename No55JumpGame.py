class Solution(object):
    def canJump(self, nums):
        if (len(nums) == 1):
            return True
            
        jump = 0
        end = 0
        farpoint = 0
        for i in range(len(nums)-1):
            if nums[i] == 0:
                return False
            farpoint = max(farpoint, i + nums[i])
            if farpoint >= len(nums) - 1:
                jump += 1
                return True
            if i == end:
                jump += 1
                end = farpoint
        return False

nums = [2,3,1,1,4]
solution = Solution()
print(solution.canJump(nums))
nums = [3,2,1,0,4]
print(solution.canJump(nums))
nums = [0,2,3]
print(solution.canJump(nums))
nums = [3,0,8,2,0,0,1]
print(solution.canJump(nums))