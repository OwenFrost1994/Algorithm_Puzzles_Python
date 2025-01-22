class Solution:
    def shortestWordDistance(self, wordsDict, word1: str, word2: str) -> int:
        # n = len(wordsDict)
        # count1 = []
        # count2 = []
        # for i in range(n):
        #     if wordsDict[i] == word1:
        #         count1.append(i)
        #     if wordsDict[i] == word2:
        #         count2.append(i)
        # mindis = n -1
        # m = len(count1)
        # n = len(count2)
        # for i in range(m):
        #     for j in range(n):
        #         if count1[i] != count2[j]:
        #             mindis = min(mindis, abs(count1[i] - count2[j]))
        # return mindis
        ans = len(wordsDict)
        if word1 == word2:
            j = -1
            for i, w in enumerate(wordsDict):
                if w == word1:
                    if j != -1: # i != -1 too, so both words found
                        ans = min(ans, i - j)
                    j = i
        else:
            i = j = -1
            for k, w in enumerate(wordsDict):
                if w == word1:
                    i = k
                if w == word2:
                    j = k
                if i != -1 and j != -1:
                    ans = min(ans, abs(i - j))
        return ans

solution = Solution()
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
print(solution.shortestWordDistance(wordsDict, word1, word2))

wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "makes"
print(solution.shortestWordDistance(wordsDict, word1, word2))