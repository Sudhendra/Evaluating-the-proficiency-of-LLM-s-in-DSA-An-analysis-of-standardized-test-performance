from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def computeHelper(left, right, operator):
            results = []
            for num1 in left:
                for num2 in right:
                    if operator == '+':
                        results.append(num1 + num2)
                    elif operator == '-':
                        results.append(num1 - num2)
                    elif operator == '*':
                        results.append(num1 * num2)
            return results
        
        if expression.isdigit():
            return [int(expression)]
        
        res = []
        for i in range(len(expression)):
            if expression[i] in ['+', '-', '*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                res += computeHelper(left, right, expression[i])
        
        return res
