from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums) -> int:
        arr = [nums.pop(0)]                  # <-- 1) initial step
        for n in nums:                       # <-- 2) iterate through nums
            if n > arr[-1]:                  # <--    2a)
                arr.append(n)
            else:                            # <--    2b)
                arr[bisect_left(arr, n)] = n 
        return len(arr)                      # <-- 3) return the length of arr

class Solution:
    def lengthOfLIS(self, nums) -> int:
        memo = {}
        def dfs(idx):
            if idx in memo:
                return memo[idx]
            
            max_val = 1
            for i in range(idx + 1, len(nums)):
                if nums[i] > nums[idx]:
                    max_val = max(max_val, dfs(i) + 1)

            memo[idx] = max_val
            return max_val

        res = 0
        for i in range(len(nums)):
            res = max(res, dfs(i))
        return res
    
solution = Solution()
nums = [10,9,2,5,3,7,101,18]
print(solution.lengthOfLIS(nums))

nums = [0,1,0,3,2,3]
print(solution.lengthOfLIS(nums))

nums = [7,7,7,7,7,7,7]
print(solution.lengthOfLIS(nums))