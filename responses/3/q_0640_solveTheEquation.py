class Solution:
    def solveEquation(self, equation: str) -> str:
        def parse(equation: str):
            equation += '='
            coeff = 0
            const = 0
            sign = 1
            num = 0
            var = 'x'
            for i in range(len(equation)):
                if equation[i] in ['+', '-', '=']:
                    if equation[i-1].isdigit():
                        const += int(equation[i-1])*sign
                    else:
                        const += sign
                    sign = 1 if equation[i] == '+' else -1
                    num = 0
                elif equation[i].isdigit():
                    num = num*10 + int(equation[i])
                elif equation[i] == 'x':
                    if num == 0:
                        coeff += sign
                    else:
                        coeff += num*sign
                    num = 0
            return coeff, const

        left_coeff, left_const = parse(equation.split('=')[0])
        right_coeff, right_const = parse(equation.split('=')[1])

        if left_coeff == right_coeff:
            if left_const == right_const:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            x_val = (right_const - left_const) / (left_coeff - right_coeff)
            return "x=" + str(int(x_val))
