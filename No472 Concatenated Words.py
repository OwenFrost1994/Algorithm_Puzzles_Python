# This is a DFS. 但是借助了前缀树，tire/digital tree/prefix tree。
# 这个树根据前缀数值往里面加深层次来搜索
# 这个节点都是一个子树，所以定义树就行，一个节点后面连着一个系列的child nodes，每一个child对应一个字母，叠几层就是一个搜索词
# 短的词要加进去，长的词进行搜索（dfs），由短词构成的长词加到result里面，处理长词就靠isend，如果到了end那就从头搜后面的部分word[i + 1:]，全true就加result

from typing import List
class Tire():
    def __init__(self) -> None:
        self.children = [None] * 26
        self.isend = False

    def insert(self, word):
        node = self
        for c in word:
            index = ord(c) - ord("a")
            if node.children[index] == None:
                node.children[index]  = Tire()
            node = node.children[index]
        node.isend = True

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dfs(word):
            if not word:
                return True
            node = tire
            for i, c in enumerate(word):
                index = ord(c) - ord("a")
                if node.children[index] == None:
                    return False
                else:
                    node = node.children[index]
                if node.isend and dfs(word[i + 1:]):
                    return True
            return False
                
        result = []
        tire = Tire()
        words.sort(key = lambda x: len(x))
        for word in words:
            if dfs(word):
                result.append(word)
            else:
                tire.insert(word)
        return result

solution = Solution()
print(solution.findAllConcatenatedWordsInADict(words = ["cat","dog","catdog"]))
print(solution.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
