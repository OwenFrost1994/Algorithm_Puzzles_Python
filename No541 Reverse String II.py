# 这里有一个遍历步长的问题，range函数可以一次跳2k
# str不能直接换位置，但是list可以

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        t = list(s)
        for i in range(0, len(s), 2*k):
            t[i : i + k] = t[i : i + k][::-1]
        return "".join(t)

solution = Solution()
print(solution.reverseStr(s = "abcdefg", k = 2))
print(solution.reverseStr(s = "abcd", k = 2))
print(solution.reverseStr(s = "abcd", k = 3))