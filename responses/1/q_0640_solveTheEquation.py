class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        def evaluate(expr):
            total = 0
            coeff = 0
            sign = 1
            i = 0
            while i < len(expr):
                if expr[i] == '+' or expr[i] == '-':
                    total += sign * int(expr[coeff:i]) if expr[coeff:i] else 0
                    coeff = i + 1
                elif expr[i] == 'x':
                    if coeff == i or expr[i-1].isdigit():
                        total += sign * int(expr[coeff:i]) if expr[coeff:i] else sign
                    else:
                        total += sign
                    coeff = i + 1
                elif expr[i].isdigit():
                    while i < len(expr) and expr[i].isdigit():
                        i += 1
                    total += sign * int(expr[coeff:i])
                    coeff = i
                    continue
                sign = 1 if expr[i] == '+' else -1
                i += 1
            total += sign * int(expr[coeff:])
            return total

        left_total, right_total = evaluate(left), evaluate(right)
        x_coeff = left_total - right_total
        num_x = sum(map(lambda x: x == 'x', equation))
        if x_coeff == 0 and num_x == 0:
            return "Infinite solutions"
        elif x_coeff == 0 and num_x != 0:
            return "No solution"
        else:
            return "x=" + str(x_coeff // num_x)
