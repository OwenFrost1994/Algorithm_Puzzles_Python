# 这里面单词有顺序的问题
from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def check(a, b):
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    j += 1
                i += 1
            return j == len(b)
        result = ""
        for word in dictionary:
            if check(s, word) and (len(result) < len(word) or (len(result) == len(word) and result > word)):
                result = word
        return result

solution = Solution()
print(solution.findLongestWord(s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))
print(solution.findLongestWord(s = "abpcplea", dictionary = ["a","b","c"]))