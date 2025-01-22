import re

class Solution:
    def solveEquation(self, equation: str) -> str:
        
        def parse(s):
            x, n = 0, 0
            for sign, num, is_x in re.findall('([+-]?)(\d*)(x?)', s):
                if is_x:
                    x += int(sign + num) if num else int(sign + '1')
                elif num:
                    n += int(sign + num)
            return x, n
            
        l_eq, r_eq = equation.split('=')
        (xl, nl), (xr, nr) = parse(l_eq), parse(r_eq)
        if xl == xr:
            if nl == nr:
                return 'Infinite solutions'
            return 'No solution'
        return f'x={(nr - nl) // (xl - xr)}'
    
solution = Solution()
print(solution.solveEquation("x+5-3+x=6+x-2"))
print(solution.solveEquation(equation = "x=x"))
print(solution.solveEquation(equation = "2x=x"))