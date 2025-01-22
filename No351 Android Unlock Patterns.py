class Solution(object):
  def numberOfPatterns(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    nums = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    position = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2]}
    self.result = 0
    def dfs(prev, visited, length):
      if m <= length <= n:
        self.result += 1
      if length == n:
        return
      for i in range(1, 10):
        if i not in visited:
          if prev in position.keys():
            xp, yp = position[prev]
            x, y = position[i]
            if (abs(x - xp) == 2 or abs(y - yp) == 2) and (abs(x - xp) != 1 and abs(y - yp) != 1):
              if nums[(x + xp) // 2][(y + yp) // 2] not in visited:
                continue
          visited.add(i)
          dfs(i, visited, length + 1)
          visited.remove(i)
      return
    dfs(0, set(), 0)
    return self.result

solution = Solution()
print(solution.numberOfPatterns(m = 1, n = 1))
print(solution.numberOfPatterns(m = 1, n = 2))
print(solution.numberOfPatterns(m = 2, n = 3))
print(solution.numberOfPatterns(m = 3, n = 4))
