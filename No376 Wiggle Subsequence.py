from typing import List
# dp method, one record the length of sublist for starting with positive
# the other one record the length of sublist for starting with the negative
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        dpp = [1] * n
        dpn = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                if dpp[i - 1] % 2 != 0:
                    dpp[i] = dpp[i - 1] + 1
                else:
                    dpp[i] = dpp[i - 1]
                if dpn[i - 1] % 2 == 0:
                    dpn[i] = dpn[i - 1] + 1
                else:
                    dpn[i] = dpn[i - 1]
            if nums[i] < nums[i - 1]:
                if dpp[i - 1] % 2 == 0:
                    dpp[i] = dpp[i - 1] + 1
                else:
                    dpp[i] = dpp[i - 1]
                if dpn[i - 1] % 2 != 0:
                    dpn[i] = dpn[i - 1] + 1
                else:
                    dpn[i] = dpn[i - 1]
            if nums[i] == nums[i - 1]:
                dpp[i] = dpp[i - 1]
                dpn[i] = dpn[i - 1]
        return max(dpp[-1], dpn[-1])
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = max(up, down + 1)
            elif nums[i] < nums[i - 1]:
                down = max(down, up + 1)
        return max(up, down)
solution = Solution()
print(solution.wiggleMaxLength(nums = [1,7,4,9,2,5]))
print(solution.wiggleMaxLength(nums = [1,17,5,10,13,15,10,5,16,8]))
print(solution.wiggleMaxLength(nums = [1,2,3,4,5,6,7,8,9]))