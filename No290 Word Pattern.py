class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(s) != len(pattern):
            return False
        match = {}
        s = s.split(" ")
        a = True
        for i in range(len(s)):
            if pattern[i] in match.keys():
                if match[pattern[i]] != s[i]:
                    a = False
                    break
            else:
                match[pattern[i]] = s[i]
        
        match = {}
        b = True
        for i in range(len(s)):
            if s[i] in match.keys():
                if match[s[i]] != pattern[i]:
                    b = False
                    break
            else:
                match[s[i]] = pattern[i]
        return a and b

solution = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(solution.wordPattern(pattern, s))
pattern = "abba"
s = "dog cat cat fish"
print(solution.wordPattern(pattern, s))
pattern = "aaaa"
s = "dog cat cat dog"
print(solution.wordPattern(pattern, s))
pattern = "abba"
s = "dog dog dog dog"
print(solution.wordPattern(pattern, s))