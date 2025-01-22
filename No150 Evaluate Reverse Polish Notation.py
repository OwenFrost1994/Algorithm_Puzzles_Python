import operator

class Solution:
    def evalRPN(self, tokens):
        operations = {
            "+": (lambda x, y: operator.add(x, y)),
            "-": (lambda x, y: operator.sub(x, y)),
            "*": (lambda x, y: operator.mul(x, y)),
            "/": (lambda x, y: int(x/y))
        }

        stack = []
        for token in tokens:    
            if token not in operations:
                stack.append(int(token))
            else:
                x = stack.pop(-2)
                y = stack.pop()
                stack.append(operations[token](x, y))
        return stack.pop()

solution = Solution()

tokens = ["2","1","+","3","*"]
print(solution.evalRPN(tokens))

tokens = ["4","13","5","/","+"]
print(solution.evalRPN(tokens))

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(solution.evalRPN(tokens))