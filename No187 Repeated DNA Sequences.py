class Solution:
    def findRepeatedDnaSequences(self, s: str):
        repeat = {}
        if len(s) < 10:
            return []
        for i in range(len(s) - 9):
            subs = s[i: i + 10]
            if subs in repeat.keys():
                repeat[subs] += 1
            else:
                repeat[subs] = 1
        result = []
        for key in repeat.keys():
            if repeat[key] > 1:
                result.append(key)
        return result

solution = Solution()

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(solution.findRepeatedDnaSequences(s))

s = "AAAAAAAAAAAAA"
print(solution.findRepeatedDnaSequences(s))