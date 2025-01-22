class Solution(object):
    def lengthOfLastWord(self, s):
        strings = s.split()
        return len(strings[-1])

s = "Hello World"
solution = Solution()
print(solution.lengthOfLastWord(s))

s = "   fly me   to   the moon  "
print(solution.lengthOfLastWord(s))

s = "luffy is still joyboy"
print(solution.lengthOfLastWord(s))