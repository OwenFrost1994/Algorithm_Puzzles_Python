class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 1
        nums = set(nums)

        nums = list(nums)
        
        nums.sort()
        longest = 1
        lenth = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i] + 1:
                lenth += 1
            else:
                longest = max(longest, lenth)
                lenth = 1
        longest = max(longest, lenth)
        return longest

from collections import defaultdict
class Solution1:
    def longestConsecutive(self, nums):
        mp=defaultdict(list)
        bl=defaultdict(bool)
        mx=0
        for i in nums:
            if bl[i]:
                continue 
            bl[i]=True
            l,r=i,i
            if mp[i+1]:
                r=mp[i+1][0]
            if mp[i-1]:
                l=mp[i-1][1]
            mp[r]=[r,l]
            mp[l]=[r,l]
            mx=max(mx,r-l+1)
        return mx
    
solution = Solution1()

nums = [100,4,200,1,3,2]
print(solution.longestConsecutive(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(solution.longestConsecutive(nums))

nums = [1,2,0,1]
print(solution.longestConsecutive(nums))