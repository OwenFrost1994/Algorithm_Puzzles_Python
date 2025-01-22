class Solution:
    def lastRemaining(self, n: int) -> int:
        n1, nn = 1, n
        i, step, num = 0, 1, n # record number of elimination, step between numbers, and number of numers
        while num > 1:
            if i % 2 == 0: # from left to right
                n1 += step
                if num % 2 != 0:
                    nn -= step
            else: # from right to left
                nn -= step
                if num % 2 != 0:
                    n1 += step
            num = num // 2
            step *= 2
            i += 1
        return nn
solution = Solution()
print(solution.lastRemaining(9))
print(solution.lastRemaining(8))
print(solution.lastRemaining(1))