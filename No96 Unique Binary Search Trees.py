class Solution:
    def numTrees(self, n: int) -> int:
        nums = [0] * (n + 1)
        nums[0] = 1
        nums[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                nums[i] += nums[i - j] * nums[j - 1]
        return nums[n]

solution = Solution()

print(solution.numTrees(1))

print(solution.numTrees(2))

print(solution.numTrees(3))