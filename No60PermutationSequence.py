# class Solution:
#     def getPermutation(self, n, k):
#         results = []
#         nums = list(range(1,n + 1))

#         self.Permutation(nums[:], results, 0)
        
#         results.sort(key = lambda x:[x[i] for i in range(len(nums)-1)])
#         result = ""
#         for i in range(len(results[k-1])):
#             result = result + str(results[k-1][i])
        
#         return result

#     def Permutation(self, nums, results, index):
#         if (index == len(nums)):
#             results.append(nums[:])
        
#         for i in range(index, len(nums)):
#             nums[i], nums[index] = nums[index], nums[i]
#             self.Permutation(nums, results, index + 1)
#             nums[i], nums[index] = nums[index], nums[i]

class Solution:
    def getPermutation(self, n, k):
        fact = 1
        nums = list(range(1, n + 1))
        
        for i in range(1, n):
            fact *= i
        
        ans = []
        k -= 1
        
        while True:
            ans.append(str(nums[k // fact]))
            nums.pop(k // fact)
            
            if not nums:
                break
            
            k %= fact
            fact //= len(nums)
        
        return ''.join(ans)
n = 3
k = 5
solution = Solution()
print(solution.getPermutation(n, k))

n = 4
k = 9
print(solution.getPermutation(n, k))

n = 3
k = 1
print(solution.getPermutation(n, k))