from collections import defaultdict

class Solution:
    def groupStrings(self, strings):
        results = {}
        for s in strings:
            offset = ord(s[0]) - ord("a")
            t = ""
            for c in s:
                cd = ord(c) - offset
                if cd < ord("a"):
                    cd += 26
                t += chr(cd)
            if t not in results.keys():
                results[t] = [s]
            else:
                results[t].append(s)
        return list(results.values())

class Solution:
    def groupStrings(self, strings):
        results = {}
        for s in strings:
            lenth = len(s)
            pattern = "0"
            for i in range(1, lenth):
                pattern += str(ord(s[i]) - ord(s[i - 1]))
            key = str(lenth) + "->" + pattern
            if key not in results.keys():
                results[key] = [s]
            else:
                results[key].append(s)
        return list(results.values())

solution = Solution()
print(solution.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"]))
print(solution.groupStrings(["a"]))
