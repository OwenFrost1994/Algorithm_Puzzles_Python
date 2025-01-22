# 1,2 only have 1 cases 2,1
# 1,2,3 have 2 cases 3,1,2 2,3,1
# 1,2,3,4 have 4,3,1,2 3,4,1,2 3,1,4,2 (4,3,2,1 3,4,2,1, 2,1,4,3) 2,3,4,1  2,4,1,3 4,1,2,3

class Solution:
    def findDerangement(self, n: int) -> int:
        mod = 10**9 + 7
        a, b = 1, 0
        for i in range(2, n + 1):
            a, b = b, ((i - 1) * (a + b)) % mod
        return b

solution = Solution()
print(solution.findDerangement(n = 3))
print(solution.findDerangement(n = 2))
print(solution.findDerangement(n = 4))