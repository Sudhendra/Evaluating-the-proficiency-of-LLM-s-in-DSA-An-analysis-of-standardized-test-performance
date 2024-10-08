class Solution:
    
    def solveEquation(self, equation: str) -> str:
        def evaluate(expression: str) -> tuple:
            l_coef, l_const = 0, 0
            term = ''
            sign = 1
            for char in expression+'=':
                if char in '+-=':
                    if term:
                        if term[-1] == 'x':
                            if len(term) == 1:
                                l_coef += sign
                            else:
                                l_coef += int(term[:-1]) * sign
                        else:
                            l_const += int(term) * sign
                    if char == '=':
                        break
                    term = ''
                    sign = 1 if char == '+' else -1
                else:
                    term += char
            return l_coef, l_const
    
        left_coef, left_const = evaluate(equation.split('=')[0])
        right_coef, right_const = evaluate(equation.split('=')[1])
        
        coef_diff = left_coef - right_coef
        const_diff = right_const - left_const
        
        if coef_diff == 0:
            if const_diff == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        
        return f"x={const_diff // coef_diff}"
