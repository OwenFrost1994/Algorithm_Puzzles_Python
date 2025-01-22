# "aaa" -> "3[a]"其实不必原来的短，因此不需要encode
# "aaaaa" -> "5[a]"
# "aaaaaaaaaa" -> "10[a]"
# "aabcaabcd" -> "2[aabc]d"
# "abbbabbbcabbbabbbc" -> "2[2[abbb]c]"
# 这个不能直接进行遍历如果进行直接遍历"aaabaaaaaabaaa"可能是"aaab6[a]baaa"但实际上是"2[aaabaaa]"
# 这里利用了一个trick, 我们双倍str 2*str,看str从哪里开始重复substr也就找到了string看No459
# 但是还有两个问题,1. 重复的str内部也可能继续被压缩,也就需要recursion重复的字段substr再压缩，类似"2[2[abbb]c]"
# 2.这样直接看找重复的字符串不等于就是最短的,办法是从中间切开,看left和right进行"分治",看拼起来是不是比起直接连接最短，类似"2[aabc]d"直接就不是一个重复字符串

class Solution:
    def encode(self, s: str, dp = {}) -> str:
        if len(s) < 5:
            return s
        elif s in dp:
            return dp[s] # the compression is already found
        dp[s] = s
        index = (s + s).find(s, 1)
        if 0 <= index < len(s):
            dp[s] = str(len(s) // index) + "[" + self.encode(s[:index], dp)  +"]" 
        for i in range(1, len(s)): # no need to start from zero， cause 0：end is s，this has been tested
            left = self.encode(s[:i], dp)
            right = self.encode(s[i:], dp)
            if len(left) + len(right) < len(dp[s]):
                dp[s] = left + right
        return dp[s]

solution = Solution()
# print(solution.encode("aaa"))
# print(solution.encode("aaaaa"))
# print(solution.encode("aaaaaaaaaa"))
print(solution.encode("aabcaabc"))
print(solution.encode("aabcaabcd"))
print(solution.encode("abbbabbbcabbbabbbc"))
print(solution.encode("slkjdfbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"))