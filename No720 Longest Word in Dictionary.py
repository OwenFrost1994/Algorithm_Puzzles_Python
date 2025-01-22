# 这个是个很苯的便利问题，word的前n位在不在set里面，一个办法是前缀树但是太复杂了

from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words = set(words)
        result = ""
        maxlen = 0
        for w in words:
            n = len(w)
            if all([w[:i] in words for i in range(1, n)]): #not starting from 0 but 1
                if maxlen < n or (maxlen == n and w < result):
                    maxlen, result = n, w
        return result

solution = Solution()
print(solution.longestWord(words = ["w","wo","wor","worl","world"]))
print(solution.longestWord(words = ["a","banana","app","appl","ap","apply","apple"]))