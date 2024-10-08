class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        left_x, left_val = self.parse_equation(left)
        right_x, right_val = self.parse_equation(right)

        x_coef = left_x - right_x
        val = right_val - left_val

        if x_coef == 0:
            if val == 0:
                return "Infinite solutions"
            else:
                return "No solution"

        x_val = val / x_coef
        return "x=" + str(int(x_val))

    def parse_equation(self, equation: str):
        equation += '+'
        num, coef = "", 0
        x, val = 0, 0
        sign = 1

        for char in equation:
            if char.isdigit():
                num += char
            elif char == 'x':
                if num == "":
                    coef += sign
                else:
                    coef += sign * int(num)
                num = ""
                x += coef
            else:
                if num:
                    val += sign * int(num)
                    num = ""

                if char == '+':
                    sign = 1
                elif char == '-':
                    sign = -1

        return x, val
