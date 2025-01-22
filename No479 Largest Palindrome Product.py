# 先找一个回文数，然后再看有没有n位的数字能整除
# 对n位的数字，回文数肯定是2n位，n=2，最大的回文数是99-99，之后是98-89，97-79，96-69，这是因为从大到小排序
# 能否整除也从类似的数从大到小开始找

class Solution:
    def largestPalindrome(self, n: int) -> int:
        maxn = 10**n - 1
        for num in range(maxn, 10**(n - 1) - 1, -1):
            b = num
            x = num
            while b > 0:
                x = x * 10 + b % 10
                b = b // 10
            a = maxn
            while a * a >= x:
                if x % a == 0:
                    return x % 1337
                a -= 1
        return 9

solution = Solution()
print(solution.largestPalindrome(1))
print(solution.largestPalindrome(2))
print(solution.largestPalindrome(3))