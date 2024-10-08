from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        result = []
        for i in range(len(expression)):
            if expression[i] in "+-*":
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])
                for left in left_results:
                    for right in right_results:
                        if expression[i] == '+':
                            result.append(left + right)
                        elif expression[i] == '-':
                            result.append(left - right)
                        elif expression[i] == '*':
                            result.append(left * right)

        return result
