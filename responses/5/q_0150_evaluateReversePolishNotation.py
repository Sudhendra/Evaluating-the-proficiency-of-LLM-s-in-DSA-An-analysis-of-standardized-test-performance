from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(['+', '-', '*', '/'])

        for token in tokens:
            if token in operators:
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = self.evaluate(token, int(operand1), int(operand2))
                stack.append(str(result))
            else:
                stack.append(token)

        return int(stack.pop())

    def evaluate(self, operator, operand1, operand2):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            return int(operand1 / operand2)
