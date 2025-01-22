# https://leetcode.com/problems/different-ways-to-add-parentheses/solutions/4065987/recursive-python-solution-using-eval/
# https://leetcode.com/problems/different-ways-to-add-parentheses/solutions/1294189/easy-solution-faster-than-100-explained-with-diagrams/

class Solution:
    def diffWaysToCompute(self, expression: str):
        result = []
        operators = "*-+"
        isNumber = True
        for op in operators:
            if op in expression:
                isNumber = False
        if isNumber:
            return [int(expression)]
        for i,c in enumerate(expression):
            if c in operators:
                res1 = self.diffWaysToCompute(expression[:i])
                res2 = self.diffWaysToCompute(expression[i + 1:])
                for r1 in res1:
                    for r2 in res2:
                        result.append(eval(str(r1) + c + str(r2)))
        return result
    
class Solution1:
    def diffWaysToCompute(self, expression: str):
        # operations map
        operation = {'*' : lambda x,y: x*y, '+' : lambda x,y: x+y, '-' : lambda x,y: x-y}

        def helper(expression):
            result = []
            for i, x in enumerate(expression):
                if x in ('+', '-', '*'):
                    leftResult = helper(expression[0:i]) # list of results for the left expression(s)
                    rightResult = helper(expression[i+1:]) # list of results for the right expression(s)
                    # append all the combinations
                    for leftValue in leftResult:
                        for rightValue in rightResult:
                            result.append(operation[x](leftValue, rightValue))
            return result if result else [int(expression)] # if result list is empty => expression is the single number
        return helper(expression)
    
class Solution2:
    def diffWaysToCompute(self, expression: str):
        operation = {"*": lambda x, y: x*y, "+": lambda x, y: x + y, "-": lambda x, y: x - y}

        def opertree(expression):
            result = []
            for i in range(len(expression)):
                if expression[i] in operation:
                    leftresult = opertree(expression[:i])
                    rightresult = opertree(expression[i+1:])
                    for leftval in leftresult:
                        for rightval in rightresult:
                            result.append(operation[expression[i]](leftval, rightval))
            if result:
                return result
            else:
                return [int(expression)]
        return opertree(expression)
    
solution = Solution2()
expression = "2-1-1"
print(solution.diffWaysToCompute(expression))

expression = "2*3-4*5"
print(solution.diffWaysToCompute(expression))