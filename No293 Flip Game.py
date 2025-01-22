class Solution(object):
  def generatePossibleNextMoves(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    ans = []
    n = len(s)
    for i in range(n - 1):
      if s[i: i + 2] == "++":
        ans.append(s[:i] + "--" + s[i + 2:])
    return ans

solution = Solution()
print(solution.generatePossibleNextMoves("++++"))
print(solution.generatePossibleNextMoves("+"))