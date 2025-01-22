from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums) -> str:
        def comp(x, y):
            return int(str(y) + str(x)) - int(str(x) + str(y))
        
        sorted_numbers = sorted(nums, key=cmp_to_key(comp))
        # ans = ''.join(str(i) for i in sorted_numbers)
        ans = ""
        for i in range(len(sorted_numbers)):
            if i > 0 and str(sorted_numbers[i]) == "0" and ans[0] == "0":
                pass
            else:
                ans = ans + str(sorted_numbers[i])
        return ans
    
solution = Solution()
nums = [0,0]
print(solution.largestNumber(nums))

nums = [10,2]
print(solution.largestNumber(nums))

nums = [3,30,34,5,9]
print(solution.largestNumber(nums))