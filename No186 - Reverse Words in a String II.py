class Solution:
    def reverseWords(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(i, j, s):
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        
        i = 0
        j = 0
        n = len(s)
        while j < n:
            if s[j] == " ":
                reverse(i, j - 1, s)
                i = j + 1
            if j == n - 1:
                reverse(i, j, s)
            j += 1
        reverse(0, n - 1, s)
solution = Solution()
s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
print(solution.reverseWords(s))
print(s)
s = ["a"]
print(solution.reverseWords(s))
print(s)