class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = "+"
        s += "+"  # To handle the last number or operator
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] != " ":
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack[-1] = stack[-1] * num
                elif sign == "/":
                    stack[-1] = int(stack[-1] / num)
                num = 0
                sign = s[i]
        return sum(stack)
