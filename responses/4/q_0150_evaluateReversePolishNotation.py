from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token in operators:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    result = num1 + num2
                elif token == '-':
                    result = num1 - num2
                elif token == '*':
                    result = num1 * num2
                else:  # division truncates toward zero
                    result = int(num1 / num2)
                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()
