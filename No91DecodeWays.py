# class Solution:
#     wordmap = {"1": "A", "2": "B","3": "C", "4": "D", "5": "E", "6": "F", "7": "G", "8": "H", "9": "I", "10": "J", "11": "K", "12": "L", "13": "M",
#                "14": "N", "15": "O", "16": "P", "17": "Q", "18": "R", "19": "S", "20": "T", "21": "U", "22": "V", "23": "W", "24": "X", "25": "Y", "26": "Z"}
#     def numDecodings(self, s):
#         results = []
#         self.translate(s, "", results, 0)
#         return len(results)
#     def translate(self, s, result, results, index):
#         if index >= len(s):
#             results.append(result)
#             return
        
#         subs = s[index: index + 1]
#         if subs in self.wordmap.keys():
#             self.translate(s, result + self.wordmap[subs], results, index + 1)

#         if index < len(s) - 1:
#             subs = s[index: index + 2]
#             if subs in self.wordmap.keys():
#                 self.translate(s, result + self.wordmap[subs], results, index + 2)
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        # dp[i]: number of ways of decoding the substring s[:i]
        dp = [0 for _ in range(n + 1)]
        # base case
        dp[0] = 1
        for i in range(1, n + 1):
            # check single digit decode
            # valid deocde is possible only when s[i - 1] is not zero
            # if so, take the previous state dp[i - 1]
            # e.g. AB - 1[2]
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            # check double digit decode
            # by looking at the previous two digits
            # if the substring belongs to the range [10 - 26]
            # then add the previous state dp[i - 2]
            # e.g. L - [12]
            if i >= 2:
                # or you can use `stoi(s.substr(i - 2, 2))`
                x = int(s[i - 2: i])
                # check the range
                if 10 <= x <= 26:
                    dp[i] += dp[i - 2]
        return dp[n]

solution = Solution()

s = "12"
print(solution.numDecodings(s))

s = "226"
print(solution.numDecodings(s))

s = "06"
print(solution.numDecodings(s))