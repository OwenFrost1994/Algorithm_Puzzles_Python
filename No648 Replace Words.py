# 前缀树搜索

from collections import defaultdict
from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tire = defaultdict()
        for word in dictionary:
            cur = tire
            for c in word:
                if c not in cur.keys():
                    cur[c] = defaultdict()
                cur = cur[c]
            cur["$"] = True
        newsent = []
        for word in sentence.split():
            cur = tire
            root = ""
            for c in word:
                if "$" in cur.keys():
                    break
                if c not in cur.keys():
                    break
                cur = cur[c]
                root += c
            if "$" in cur.keys():
                newsent.append(root)
            else:
                newsent.append(word)
        return " ".join(newsent)
    
solution = Solution()
print(solution.replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
print(solution.replaceWords(dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"))