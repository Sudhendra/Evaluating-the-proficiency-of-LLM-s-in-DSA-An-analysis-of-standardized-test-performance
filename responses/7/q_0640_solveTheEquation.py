class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        x_coeff_left, const_left = self.evaluateExpression(left)
        x_coeff_right, const_right = self.evaluateExpression(right)
        
        x_coeff = x_coeff_left - x_coeff_right
        const = const_right - const_left
        
        if x_coeff == 0:
            if const == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x_value = const // x_coeff
            return "x=" + str(x_value)
    
    def evaluateExpression(self, expression: str) -> Tuple[int, int]:
        x_coeff = 0
        constant = 0
        
        sign = 1
        operand = 0
        is_x_coefficient = False
        
        for i in range(len(expression)):
            char = expression[i]
            
            if char in ['+', '-']:
                constant += sign * operand
                operand = 0
                is_x_coefficient = False
                
                if char == '-':
                    sign = -1
                else:
                    sign = 1
            elif char == 'x':
                if operand == 0:
                    operand = 1
                x_coeff += sign * operand
                operand = 0
                is_x_coefficient = True
            else:
                operand = operand * 10 + int(char)
        
        if is_x_coefficient:
            x_coeff += sign * operand
        else:
            constant += sign * operand
        
        return x_coeff, constant
