class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result = []
        position = {}
        for i in range(len(s)):
            position[s[i]] = i
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                while (result and result[-1] > s[i]) and position[result[-1]] > i:
                    visited.remove(result.pop())
                result.append(s[i])
                visited.add(s[i])
        return "".join(result)
    
solution = Solution()
print(solution.removeDuplicateLetters("bcabc"))
print(solution.removeDuplicateLetters("cbacdcbc"))