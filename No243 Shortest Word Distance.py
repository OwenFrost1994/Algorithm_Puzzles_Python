class Solution(object):
  def shortestDistance(self, words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    n = len(words)
    i = -1
    j = -1
    mindis = n - 1
    for k in range(n):
        if words[k] == word1:
            i = k
        if words[k] == word2:
            j = k
        if i != -1 and j != -1:
           mindis = min(mindis, abs(i - j))
    return mindis
  
solution = Solution()
wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "coding"
word2 = "practice"
print(solution.shortestDistance(wordsDict, word1, word2))

wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
word1 = "makes"
word2 = "coding"
print(solution.shortestDistance(wordsDict, word1, word2))