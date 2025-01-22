# num = 5
# num          = 00000101
# mask         = 11111000
# ~mask & ~num = 00000010
# num = 9
# num          = 00000101
# mask         = 00000111
# mask ^ num   = 00000010
class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num

solution = Solution()
print(solution.findComplement(5))
print(solution.findComplement(2))
print(solution.findComplement(9))