from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        
        result = []
        for i in range(len(expression)):
            if expression[i] in "+-*":
                left_part = self.diffWaysToCompute(expression[:i])
                right_part = self.diffWaysToCompute(expression[i+1:])
                for l in left_part:
                    for r in right_part:
                        if expression[i] == "+":
                            result.append(l + r)
                        elif expression[i] == "-":
                            result.append(l - r)
                        elif expression[i] == "*":
                            result.append(l * r)
        
        return result
