from typing import List

class Solution:

    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            res = []
            for l in left:
                for r in right:
                    if op == '+':
                        res.append(l + r)
                    elif op == '-':
                        res.append(l - r)
                    elif op == '*':
                        res.append(l * r)
            return res
        
        if expression.isdigit():
            return [int(expression)]
        
        res = []
        for i, char in enumerate(expression):
            if char in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                res.extend(compute(left, right, char))
        
        return res
