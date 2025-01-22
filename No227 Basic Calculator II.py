import operator
from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        highoperations = {
            "*": (lambda x, y: operator.mul(x, y)),
            "/": (lambda x, y: int(x/y))
        }
        lowoperations = {
            "+": (lambda x, y: operator.add(x, y)),
            "-": (lambda x, y: operator.sub(x, y)),
        }

        s = "".join(s.split(" "))

        stacknums = deque()
        stackopes = deque()
        i = 0
        while i < len(s):
            if s[i].isdigit():
                j = self.findnum(s, i)
                stacknums.append(int(s[i:j]))
                i = j
                continue
            if s[i] in lowoperations:
                stackopes.append(s[i])
                i = i + 1
                continue
            if s[i] in highoperations:
                oper = s[i]
                x = stacknums.pop()
                i = i + 1
                j = self.findnum(s, i)
                y = int(s[i:j])
                stacknums.append(highoperations[oper](x, y))
                i = j
            
        while stackopes:
            x = stacknums.popleft()
            y = stacknums.popleft()
            oper = stackopes.popleft()
            stacknums.appendleft(lowoperations[oper](x, y))
        return stacknums.pop()
    
    def findnum(self, s, i):
        j = i
        while j < len(s) and s[j].isdigit() :
            j = j + 1
        return j
    
solution = Solution()

# s = "3+2*2"
# print(solution.calculate(s))

# s = "3/2"
# print(solution.calculate(s))

s = "1-1+1"
print(solution.calculate(s))

s = "1+1+1"
print(solution.calculate(s))

s = " 3+5 / 2 "
print(solution.calculate(s))

s = "42"
print(solution.calculate(s))