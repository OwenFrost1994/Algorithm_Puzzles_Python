# a^b % 1337 = ((a % 1337)^b) % 1337
# (x * y) % 1337 = ((x % 1337) * (y % 1337)) % 1337
# (a^(bcd)) % 1337 = (a^(100b + 10c + d)) % 1337 = (a^(100b)*a^(10c)*a^(d)) % 1337 = (a^(100b)*a^(10c)*a^(d) % 1337
# = (a^(100b) % 1337) * ((a^(10c) % 1337) * (a^(d) % 1337) % 1337)
from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        result = 1
        MOD = 1337
        for num in b[::-1]:
            result = result * pow(a, num, MOD) % MOD
            a = pow(a, 10 ,MOD)
        return result
    
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        ret = 1
        k = 1
        for num in reversed(b):
            ret *= a ** (num) % 1337
            a = a ** 10 % 1337
        return ret % 1337

solution = Solution()
print(solution.superPow(a = 2, b = [3]))
print(solution.superPow(a = 2, b = [1,0]))
print(solution.superPow(a = 1, b = [4,3,3,8,5,2]))