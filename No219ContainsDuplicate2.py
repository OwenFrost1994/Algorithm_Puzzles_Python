class Solution:
    def simplifyPath(self, nums, k):
        if len(set(nums)) == len(nums):
            return False
        if k==0:
            return True
        numset = set()

        for i in range(len(nums)):
            if nums[i] in numset:
                return True
            numset.add(nums[i])
            if len(numset) > k:
                numset.remove(nums[i-k])
        return False
nums = [1,2,3,1]
k = 3
solution = Solution()
print(solution.containsNearbyDuplicate(nums, k))

nums = [1,0,1,1]
k = 1
print(solution.containsNearbyDuplicate(nums, k))

nums = [1,2,3,1,2,3]
k = 2
print(solution.containsNearbyDuplicate(nums, k))