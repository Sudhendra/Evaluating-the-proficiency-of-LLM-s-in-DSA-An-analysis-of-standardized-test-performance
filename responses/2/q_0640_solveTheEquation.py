class Solution:
    def solveEquation(self, equation: str) -> str:
        def evaluate_expression(exp):
            variables = 0
            constants = 0
            sign = 1
            i = 0
            while i < len(exp):
                if exp[i] == 'x':
                    if i == 0 or exp[i - 1] in ['+', '-']:
                        variables += sign
                    else:
                        variables += sign * int(exp[:i])
                    exp = exp[i+1:]
                    i = 0
                elif exp[i] in ['+', '-']:
                    constants += sign * int(exp[:i])
                    sign = 1 if exp[i] == '+' else -1
                    exp = exp[i+1:]
                    i = 0
                else:
                    i += 1
            constants += sign * int(exp)
            return variables, constants
        
        left, right = equation.split('=')
        left_vars, left_consts = evaluate_expression(left)
        right_vars, right_consts = evaluate_expression(right)
        
        total_vars = left_vars - right_vars
        total_consts = right_consts - left_consts
        
        if total_vars == 0:
            return "Infinite solutions" if total_consts == 0 else "No solution"
        
        solution = total_consts // total_vars
        return "x=" + str(solution)