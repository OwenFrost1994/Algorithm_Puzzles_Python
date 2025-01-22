from collections import Counter
class Solution:
    def findErrorNums(self, nums):
        c=Counter(nums)
        l=[0,0]
        for i in range(1,len(nums)+1):
            if c[i]==2:
                l[0]=i
            if c[i]==0:
                l[1]=i
        return l
solution = Solution()
print(solution.findErrorNums([1,2,2,4]))
print(solution.findErrorNums([1,1]))
print(solution.findErrorNums([2,2]))