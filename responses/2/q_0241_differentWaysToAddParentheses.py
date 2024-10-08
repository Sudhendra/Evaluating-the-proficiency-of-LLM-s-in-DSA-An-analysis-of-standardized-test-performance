from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    if op == '+':
                        results.append(l + r)
                    elif op == '-':
                        results.append(l - r)
                    elif op == '*':
                        results.append(l * r)
            return results
        
        if expression.isdigit():
            return [int(expression)]
        
        res = []
        for idx, char in enumerate(expression):
            if char in "+-*":
                left_part = self.diffWaysToCompute(expression[:idx])
                right_part = self.diffWaysToCompute(expression[idx+1:])
                res.extend(compute(left_part, right_part, char))
        
        return res
