class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        for l in moves:
            if l == "U":
                x -= 1
            if l == "D":
                x += 1
            if l == "R":
                y -= 1
            if l == "L":
                y += 1
        return x == 0 and y == 0

solution = Solution()
print(solution.judgeCircle(moves = "UD"))
print(solution.judgeCircle(moves = "LL"))