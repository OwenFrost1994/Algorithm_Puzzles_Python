from typing import List

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array to make it easier to check the triangle inequality
        n = len(nums)
        count = 0
        s = 0
        while s < n and nums[s] == 0:
            s += 1
        # Loop through all possible combinations of triplets
        for i in range(s, n - 2):
            k = i + 2
            for j in range(i + 1, n - 1):
                # Increment the pointer k until the triangle inequality is not satisfied
                while k < n and nums[i] + nums[j] > nums[k]:
                    k += 1
                # Any element between j and k-1 can form a valid triangle with nums[i] and nums[j]
                count += k - j - 1

        return count

solution = Solution()
print(solution.triangleNumber(nums = [2,2,3,4]))
print(solution.triangleNumber(nums = [4,2,3,4]))
print(solution.triangleNumber(nums = [7,0,0,0]))
