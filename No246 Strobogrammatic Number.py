class Solution(object):
    def isStrobogrammatic(self, num):
        legal = {"0", "1", "8", "6", "9"}
        switch = {"0": "0", "1": "1", "8": "8", "6": "9", "9": "6"}
        nums = list(num)
        if len(set(nums) - set(legal)) > 0:
            return False
        nums.reverse()
        nums = [switch[x] for x in nums]
        if "".join(nums) == num:
            return True
        else:
            return False

  
solution = Solution()
print(solution.isStrobogrammatic("69"))

print(solution.isStrobogrammatic("88"))

print(solution.isStrobogrammatic("962"))