class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        left_x, left_num = self.calculate(left)
        right_x, right_num = self.calculate(right)
        
        x_coef = left_x - right_x
        num_val = right_num - left_num
        
        if x_coef == 0:
            if num_val == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        
        x_val = num_val // x_coef
        return "x=" + str(x_val)
    
    def calculate(self, expr: str) -> tuple:
        x_coef, num_val = 0, 0
        sign, num = 1, 0
        
        for i in range(len(expr)):
            if expr[i] == 'x':
                if i == 0 or not expr[i-1].isdigit():
                    x_coef += sign
                else:
                    x_coef += sign * int(expr[num:i])
                num = i + 1
            elif expr[i] == '+':
                num_val += sign * int(expr[num:i])
                num = i + 1
                sign = 1
            elif expr[i] == '-':
                num_val += sign * int(expr[num:i])
                num = i + 1
                sign = -1
        
        num_val += sign * int(expr[num:])
        return x_coef, num_val
