class Solution:
    def findContestMatch(self, n: int) -> str:
        teams = [str(i + 1) for i in range(n)]
        while n > 1:
            for i in range(n // 2):
                teams[i] = "(" + teams[i] + "," + teams[n - i - 1] + ")"
            n = n // 2
        return teams[0]

solution = Solution()
print(solution.findContestMatch(n = 2))
print(solution.findContestMatch(n = 4))
print(solution.findContestMatch(n = 8))
print(solution.findContestMatch(n = 16))