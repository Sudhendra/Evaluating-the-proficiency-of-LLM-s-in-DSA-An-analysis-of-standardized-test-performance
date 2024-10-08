class Solution:
    def solveEquation(self, equation: str) -> str:
        def evaluateExpression(expression):
            count_x = 0
            total = 0
            expression += "+"
            sign = 1
            num = 0
            for i in range(len(expression)):
                if expression[i] in ['+', '-']:
                    if num != 0:
                        if expression[i-1] == "x":
                            count_x += num * sign
                        else:
                            total += num * sign
                        num = 0
                    sign = 1 if expression[i] == '+' else -1
                elif expression[i] == "x":
                    if num == 0:
                        num = 1
                    count_x += num * sign
                    num = 0
                else:
                    num = num * 10 + int(expression[i])
            if count_x == 0:
                return (0, 0)
            else:
                return (count_x, total)

        left, right = equation.split("=")
        count_x_left, total_left = evaluateExpression(left)
        count_x_right, total_right = evaluateExpression(right)

        diff_count_x = count_x_left - count_x_right
        diff_total = total_right - total_left

        if diff_count_x == 0:
            if diff_total == 0:
                return "Infinite solutions"
            else:
                return "No solution"
        else:
            result = diff_total // diff_count_x
            return "x=" + str(result)
