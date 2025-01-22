# 1 ... 9 (9 digits) 10 11 12 ... 99 (2*90 dights) 100 ... 999 (3*900 dights) 1000 ... 9999 (4*9000)
class Solution:
    def findNthDigit(self, n: int) -> int:
        nd = 1
        nums = 9
        while nd * nums < n:
            n -= nd*nums
            nd += 1
            nums *= 10
        result = 10 ** (nd - 1) + (n - 1) // nd
        index = (n - 1) % nd
        return int(str(result)[index])
    
solution = Solution()
print(solution.findNthDigit(3))
print(solution.findNthDigit(11))
print(solution.findNthDigit(111))
print(solution.findNthDigit(200))