class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()
        result = ""
        num = 0
        i = len(s) - 1
        while i > -1:
            if num == k:
                result = s[i] + "-" + result
                num = 1
            else:
                result = s[i] + result
                num += 1
            i -= 1
        return result
    
solution = Solution()
print(solution.licenseKeyFormatting(s ="5F3Z-2e-9-w", k = 4))
print(solution.licenseKeyFormatting(s = "2-5g-3-J", k = 2))
