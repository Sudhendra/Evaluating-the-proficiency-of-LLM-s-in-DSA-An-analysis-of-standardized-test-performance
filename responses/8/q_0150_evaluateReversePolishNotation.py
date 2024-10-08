from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+": lambda x, y: x + y,
                     "-": lambda x, y: x - y,
                     "*": lambda x, y: x * y,
                     "/": lambda x, y: int(x / y)}  # Truncates toward zero

        for token in tokens:
            if token in operators:
                y = stack.pop()
                x = stack.pop()
                stack.append(operators[token](x, y))
            else:
                stack.append(int(token))

        return stack[0]
