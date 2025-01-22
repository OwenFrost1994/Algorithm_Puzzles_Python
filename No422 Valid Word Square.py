class Solution(object):
  def validWordSquare(self, words):
    for i in range(len(words)):
      for j in range(len(words[i])):
        if j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]:
          return False
    return True

solution = Solution()
print(solution.validWordSquare(["abcd", "bnrt", "crmy", "dtye"]))
print(solution.validWordSquare(["abcd", "bnrt", "crm", "dt"]))
print(solution.validWordSquare(["ball", "area", "read", "lady"]))
