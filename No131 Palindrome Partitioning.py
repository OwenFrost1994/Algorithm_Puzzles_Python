class Solution(object):
    def partition(self, s):
        self.result = []
        self.palpart(s, 0, [])
        return self.result
    
    def palpart(self, s, i, st):
        if i == len(s):
            self.result.append(st.copy())
            return
        for j in range(i, len(s)):
            if s[i:j + 1] == "".join(reversed(s[i:j + 1])):
                st.append(s[i:j + 1])
                self.palpart(s, j + 1, st)
                st.pop()
    # def isPalindrome(self, s):
    #     i = 0
    #     j = len(s) - 1
    #     while i < j:
    #         if s[i] == s[j]:
    #             i += 1
    #             j += 1
    #         else:
    #             return False
    #     return True

solution = Solution()
s = "aab"
print(solution.partition(s))

s = "a"
print(solution.partition(s))