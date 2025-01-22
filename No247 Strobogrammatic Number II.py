# n = 0: none

# n = 1: 0, 1, 8

# n = 2: 11, 69, 88, 96

# n = 3: 101, 609, 808, 906, 111, 619, 818, 916, 181, 689, 888, 986

# n = 4: 1001, 6009, 8008, 9006, 1111, 6119, 8118, 9116, 1691, 6699, 8698, 9696, 1881, 6889, 8888, 9886, 1961, 6969, 8968, 9966

class Solution:
    def findStrobogrammatic(self, n: int):
        def dfs(s):
            if s == 0:
                return [""]
            if s == 1:
                return ["0", "1", "8"]
            result = []
            for v in dfs(s - 2):
                for l, r in ["11", "69", "88", "96"]:
                    result.append(l + v + r)
                if s != n:
                    result.append("0" + v + "0") # if s == n, we are adding 0 in the begining of numbers. And those numbers are not ok
            return result
        return dfs(n)
    
solution = Solution()
print(solution.findStrobogrammatic(0))

print(solution.findStrobogrammatic(1))

print(solution.findStrobogrammatic(2))

print(solution.findStrobogrammatic(3))

print(solution.findStrobogrammatic(4))