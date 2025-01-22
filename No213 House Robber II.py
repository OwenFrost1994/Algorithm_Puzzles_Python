class Solution:
    def rob(self, nums) -> int:
        def maxPrice(arr):
            prev = arr[0]
            prev2 = 0
            for i in range(1,len(arr)):
                take = arr[i]
                if i>1:
                    take+=prev2
                not_take =0+prev
                cur = max(take,not_take)
                prev2 = prev
                prev = cur
            return prev
        if len(nums)<=1:
            return nums[0]

        ans1 = maxPrice(nums[1:])
        ans2 = maxPrice(nums[:-1])
        return max(ans1,ans2)

solution = Solution()
nums = [2,3,2]
print(solution.rob(nums))

nums = [1,2,3,1]
print(solution.rob(nums))