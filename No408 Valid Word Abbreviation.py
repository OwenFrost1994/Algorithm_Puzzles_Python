class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        m, n = len(word), len(abbr)
        while i < m and j < n:
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            k = j
            while k < n and abbr[k].isdigit():
                k += 1
            num = abbr[j:k]
            if not num.isdigit() or num[0] == '0' or int(num) == 0:
                return False
            j = k
            i += int(num)
            if i < m and j < n:
                if word[i] == abbr[j]:
                    i += 1
                    j += 1
                    continue
                else:
                    return False
        return i == m and j == n

solution = Solution()
print(solution.validWordAbbreviation("internationalization", "i12iz4n"))
print(solution.validWordAbbreviation("apple", "a2e"))