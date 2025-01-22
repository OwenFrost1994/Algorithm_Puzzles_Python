class Solution:
    def maxProduct(self, words) -> int:
        words=list(set(words))
        n = len(words)
        maxlen = 0
        for i in range(n):
            for j in range(i+1, n):
                common = set(list(words[i])) & set(list(words[j]))
                if len(common) == 0:
                    maxlen = max(maxlen, len(words[i])*len(words[j]))
                else:
                    continue
        return maxlen
solution = Solution()
print(solution.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))
print(solution.maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))
print(solution.maxProduct(["a","aa","aaa","aaaa"]))