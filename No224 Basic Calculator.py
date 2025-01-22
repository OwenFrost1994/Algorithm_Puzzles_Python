import operator
from collections import deque

class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(i):
            res, digit, sign = 0, 0, 1
            
            while i < len(s):
                if s[i].isdigit():
                    digit = digit * 10 + int(s[i])
                elif s[i] in '+-':
                    res += digit * sign
                    digit = 0
                    sign = 1 if s[i] == '+' else -1
                elif s[i] == '(':
                    subres, i = evaluate(i+1)
                    res += sign * subres
                elif s[i] == ')':
                    res += digit * sign
                    return res, i
                i += 1

            return res + digit * sign
        
        return evaluate(0)
    
solution = Solution()


s = "1 + 1"
print(solution.calculate(s))

s = " 2-1 + 2 "
print(solution.calculate(s))

s = "(1+(4+5+2)-3)+(6+8)"
print(solution.calculate(s))
