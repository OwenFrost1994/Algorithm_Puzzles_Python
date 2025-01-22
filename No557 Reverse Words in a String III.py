class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        result = []
        for word in words:
            result.append("".join(reversed(list(word))))
        return " ".join(result)
    
solution = Solution()
print(solution.reverseWords(s = "Mr"))
print(solution.reverseWords(s = "Mr Ding"))
print(solution.reverseWords(s = "Let's take LeetCode contest"))