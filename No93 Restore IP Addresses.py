class Solution:
    def restoreIpAddresses(self, s: str):
        results = []
        self.insertdot(results, "", 0, s, 0)
        return results
    
    def insertdot(self, results, result, index, s, numdot):
        if numdot == 3:
            if self.isvalid(s[index:]):
                results.append(result + s[index:])
            return
            
        
        for i in range(index, min(index + 3, len(s))):
            if self.isvalid(s[index: i + 1]):
                self.insertdot(results, result + s[index: i + 1] + ".", i + 1, s, numdot + 1)
    
    def isvalid(self, str):
        if len(str) > 3 or len(str) == 0:
            return False
        if len(str) > 1 and str[0] == "0":
            return False
        if len(str) > 0 and int(str) > 255:
            return False
        return True
    
solution = Solution()

s = "25525511135"
print(solution.restoreIpAddresses(s))

s = "0000"
print(solution.restoreIpAddresses(s))

s = "101023"
print(solution.restoreIpAddresses(s))