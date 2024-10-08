class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        sign = '+'

        for i in range(len(s)):
            if s[i].isdigit():
                number = number * 10 + int(s[i])

            if (not s[i].isdigit() and s[i] != ' ') or i == len(s) - 1:
                if sign == '+':
                    stack.append(number)
                elif sign == '-':
                    stack.append(-number)
                elif sign == '*':
                    stack[-1] = stack[-1] * number
                else:
                    stack[-1] = int(stack[-1] / number)

                sign = s[i]
                number = 0

        return sum(stack)
