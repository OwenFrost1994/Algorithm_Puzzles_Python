class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for l in s:
            if l != "]":
                stack.append(l)
            else:
                subs = ""
                while stack and stack[-1] != "[":
                    subs = stack.pop() + subs
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(subs * int(num))
        return "".join(stack)

solution = Solution()
print(solution.decodeString("3[a]2[bc]"))
print(solution.decodeString("3[a2[c]]"))
print(solution.decodeString("2[abc]3[cd]ef"))