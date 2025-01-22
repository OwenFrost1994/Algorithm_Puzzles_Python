from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        num = 0
        den = 1
        if expression[0].isdigit():
            expression = "+" + expression
        i, n = 0, len(expression)
        while i < n:
            sign = 1
            if expression[i] == "-":
                sign = -1
            i += 1
            j = i
            while j < n and expression[j] not in "+-":
                j += 1
            a, b = expression[i:j].split("/")
            num = num*int(b) + sign*int(a)*den
            den = den*int(b)
            i = j
        z = gcd(num, den)
        return str(num//z) + "/" + str(den//z)

solution = Solution()
print(solution.fractionAddition(expression = "-1/2+1/2"))
print(solution.fractionAddition(expression = "-1/2+1/2+1/3"))
print(solution.fractionAddition(expression = "1/3-1/2"))