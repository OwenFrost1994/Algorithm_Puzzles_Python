class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num, count = x ^ y, 0
        while(num != 0):
            if num % 2 == 1:
                count += 1
            num = num // 2
        return count

solution = Solution()
print(solution.hammingDistance(x = 1, y = 4))
print(solution.hammingDistance(x = 3, y = 1))