class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split(".")
        ver2 = version2.split(".")
        i = 0
        while i < min(len(ver1), len(ver2)):
            if int(ver1[i]) < int(ver2[i]):
                return -1
            elif int(ver1[i]) > int(ver2[i]):
                return 1
            else:
                i += 1
        
        while i < len(ver1):
            if int(ver1[i]) > 0:
                return 1
            else:
                i += 1
        
        while i < len(ver2):
            if int(ver2[i]) > 0:
                return -1
            else:
                i += 1
        return 0

solution = Solution()
version1 = "1.0.1"
version2 = "1"
print(solution.compareVersion(version1, version2))

version1 = "1.01"
version2 = "1.001"
print(solution.compareVersion(version1, version2))

version1 = "1.0"
version2 = "1.0.0"
print(solution.compareVersion(version1, version2))

version1 = "0.1"
version2 = "1.1"
print(solution.compareVersion(version1, version2))