class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") >= 2:
            return False
        count = 0
        for i in range(len(s)):
            if s[i] == "L":
                count += 1
            if count == 3:
                return False
            if s[i] != "L":
                count = 0
        return True

solution = Solution()
print(solution.checkRecord("LALL"))
print(solution.checkRecord("PPALLP"))
print(solution.checkRecord("PPALLL"))