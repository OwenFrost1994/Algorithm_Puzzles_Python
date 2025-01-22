# 这个要快就需要前缀树或者用字符串比较法
from typing import List

class Tire():
    def __init__(self) -> None:
        self.child = [None]*26
        self.isend = False
    def insert(self, word):
        node = self
        for c in word:
            index = ord(c) - ord("a")
            if node.child[index] == None:
                node.child[index] = Tire()
            node = node.child[index]
        node.isend = True

class MagicDictionary:
    def __init__(self):
        self.tire = Tire()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.tire.insert(word)

    def search(self, searchWord: str) -> bool:
        def find(word, node, count, index):
            if count > 1:
                return False
            if index == len(word):
                return count <= 1 and node.isend
            c = word[index]
            ind = ord(c) - ord("a")
            # if node.child[ind] != None:
            #     return find(word, node.child[ind], count, index + 1)
            for i in range(26):
                if node.child[i] == None:
                    continue
                if find(word, node.child[i], count if i == ind else count + 1, index + 1):
                    return True
            return False
                
        return find(searchWord, self.tire, 0, 0)
    
solution = MagicDictionary()
print(solution.buildDict(["hello", "leetcode"]))
print(solution.search("hello"))
print(solution.search("hhllo"))
print(solution.search("hell"))
print(solution.search("leetcoded"))