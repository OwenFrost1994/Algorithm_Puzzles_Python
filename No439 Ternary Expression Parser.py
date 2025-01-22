# 堆栈法
class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        for l in reversed(expression):
            if l != ":" and l != "?":
                if stack and stack[-1] == "?":
                    _, a, _, b = stack.pop(), stack.pop(), stack.pop(), stack.pop()
                    stack.append(a if l == "T" else b)
                else:
                    stack.append(l)
            else:
                stack.append(l)
        return stack[-1]

solution = Solution()
print(solution.parseTernary(expression = "T?2:3"))
print(solution.parseTernary(expression = "F?1:T?4:5"))
print(solution.parseTernary(expression = "T?T?F:5:3"))
