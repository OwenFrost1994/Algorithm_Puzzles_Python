class Solution:
    def toHex(self, num: int) -> str:
        d = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        res = ""
        if num == 0:
            return "0"
        if num < 0:
            num = (1<<32) + num
        while num > 0:
            if num % 16 < 10:
                res += str(num % 16)
            else:
                res += str(d[num % 16])
            num = num // 16
        return res[::-1]
    
solution = Solution()
print(solution.toHex(26))
print(solution.toHex(-1))
print(solution.toHex(-2))
print(solution.toHex(-5))