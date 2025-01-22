# 这里用了python的set运算，如果一个set1 <= 另一个set2 意味着set1是set2的子集
from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1 = set('qwertyuiop')
        s2 = set('asdfghjkl')
        s3 = set('zxcvbnm')
        result = []
        for word in words:
            w = set(word.lower())
            if w <= s1 or w <= s2 or w <= s3:
                result.append(word)
        return result

solution = Solution()
print(solution.findWords(["Hello", "Alaska", "Dad", "Peace"]))
print(solution.findWords(words = ["omk"]))
print(solution.findWords(words = ["adsdf","sfd"]))