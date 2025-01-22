# 逆天的双指针法,中心扩散

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(n):
            left = right = i
            while left >= 0 and right <= n - 1 and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
            left, right = i, i + 1
            while left >= 0 and right <= n - 1 and s[left] == s[right]:
                result += 1
                left -= 1
                right += 1
        return result

solution = Solution()
print(solution.countSubstrings("abc"))
print(solution.countSubstrings("aaa")) #overflow
print(solution.countSubstrings("abb"))
print(solution.countSubstrings("abbc"))
print(solution.countSubstrings("abba"))