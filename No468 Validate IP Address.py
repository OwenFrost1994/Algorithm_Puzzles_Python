class Solution(object):
    def validIPAddress(self, queryIP):
        nums = [str(i) for i in range(0, 10)]
        letters = ["a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]
        v6d = set(nums + letters)
        v4d = set(nums)
        v4 = queryIP.split(".")
        v6 = queryIP.split(":")
        if len(v4) == 4:
            for seg in v4:
                if seg == "" or (seg[0] == "0" and len(seg) > 1):
                    return "Neither"
                if not set(seg) <= v4d:
                    return "Neither"
                if int(seg) > 255:
                    return "Neither"
            return "IPv4"
        elif len(v6) == 8:
            for seg in v6:
                if seg == "" or len(seg) > 4:
                    return "Neither"
                if not set(seg) <= v6d:
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"

solution = Solution()
print(solution.validIPAddress(queryIP = "172.16.254.1"))
print(solution.validIPAddress(queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"))
print(solution.validIPAddress(queryIP = "256.256.256.256"))
print(solution.validIPAddress(queryIP = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
print(solution.validIPAddress(queryIP = "2001:db8:85a3:0:0:8A2E:0370:7334"))
print(solution.validIPAddress(queryIP = "2001:0db8:85a3::8A2E:037j:7334"))
print(solution.validIPAddress(queryIP = "02001:0db8:85a3:0000:0000:8a2e:0370:7334"))