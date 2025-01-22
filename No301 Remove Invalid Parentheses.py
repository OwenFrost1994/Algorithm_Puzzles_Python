from typing import List
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def dfs(index, l, r, lcnt, rcnt, ns):
            if index == n:
                if l == 0 and r == 0:
                    results.add(ns)
                return
            if n - index < r + l or lcnt < rcnt:
                return
            if s[index] == "(" and l:#remove left
                dfs(index + 1, l - 1, r, lcnt, rcnt, ns)
            elif s[index] == ")" and r:#remove right
                dfs(index + 1, l, r - 1, lcnt, rcnt, ns)
            # do nothing
            dfs(index + 1, l, r, lcnt + int(s[index] == "("), rcnt + int(s[index] == ")"), ns + s[index])
            # if s[index] == "(":
            #     dfs(index + 1, l, r, lcnt + 1, rcnt, ns + s[index])
            # elif s[index] == ")":
            #     dfs(index + 1, l, r, lcnt, rcnt + 1, ns + s[index])
            # else:
            #     dfs(index + 1, l, r, lcnt, rcnt, ns + s[index])
        l = 0
        r = 0
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == "(":
                stack.append(s[i])
                l += 1
            elif s[i] == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                    l -= 1
                else:
                    stack.append(s[i])
                    r += 1
        results = set()
        dfs(0, l, r, 0, 0, "")
        return list(results)

solution = Solution()
print(solution.removeInvalidParentheses("()())()"))
print(solution.removeInvalidParentheses("(a)())()"))
print(solution.removeInvalidParentheses(")("))