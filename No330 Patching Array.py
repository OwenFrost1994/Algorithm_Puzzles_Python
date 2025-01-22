class Solution(object):
  def minPatches(self, nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: int
    """
    i = 0
    patches = 0
    miss = 1
    while miss <= n:
      if i < len(nums) and nums[i] <= miss:
        miss += nums[i]
        i += 1
      else:
        miss += miss
        patches += 1
    return patches
  
solution = Solution()
print(solution.minPatches(nums = [1,3], n = 6))
print(solution.minPatches(nums = [1,5,10], n = 20))
print(solution.minPatches(nums = [1,2,2], n = 5))