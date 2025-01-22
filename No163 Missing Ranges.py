class Solution:
    def findMissingRanges(self, nums, lower: int, upper: int):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        # result = []
        # n = len(nums)
        # for i in range(n):
        #     if i == 0:
        #         if nums[i] > lower + 1:
        #             result.append(str(lower) + "->" + str(nums[i] - 1))
        #     if i < n - 1 and nums[i] + 1 != nums[i+1]:
        #         result.append(str(nums[i] + 1) + "->" + str(nums[i+1] - 1))
        #     if i == n - 1:
        #         if nums[i] < upper - 1:
        #             result.append(str(nums[i] + 1) + "->" + str(upper))
        # return result
        result = []
        n = len(nums)
        if n == 0:
            result.append([lower, upper])
        for i in range(n):
            if i == 0:
                if nums[i] > lower + 1:
                    result.append([lower, nums[i] - 1])
                if nums[i] == lower + 1:
                    result.append([lower, lower])
            if i < n - 1 and nums[i] + 1 != nums[i+1]:
                result.append([nums[i] + 1, nums[i+1] - 1])
            if i == n - 1:
                if nums[i] < upper - 1:
                    result.append([nums[i] + 1, upper])
                if nums[i] == upper - 1:
                    result.append([upper, upper])
        return result
solution = Solution()
print(solution.findMissingRanges([-1], lower = -2, upper = -1))
print(solution.findMissingRanges([-1], lower = -1, upper = 0))
print(solution.findMissingRanges([], lower = 1, upper = 1))
print(solution.findMissingRanges([0,1,3,50,75], lower = 0, upper = 99))
print(solution.findMissingRanges([-1], lower = -1, upper = -1))