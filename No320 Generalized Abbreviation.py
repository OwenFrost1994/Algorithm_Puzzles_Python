from typing import List

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        def dfs(index, abb):
            if index == n:
                result.append("".join(abb))
                return
            # loop for transfering letters into number
            for i in range(index + 1, n + 1):
                # print(i, word[:i])
                abb.append(str(i - index))
                if i < n:
                    abb.append(word[i])
                    dfs(i + 1, abb)
                    abb.pop()
                else:
                    dfs(i, abb)
                abb.pop()
            abb.append(word[index])
            dfs(index + 1, abb)
            abb.pop()
        
        result = []
        n = len(word)
        dfs(0, [])
        return result

solution = Solution()
print(solution.generateAbbreviations("word"))
print(solution.generateAbbreviations("a"))
print(solution.generateAbbreviations("abcde"))