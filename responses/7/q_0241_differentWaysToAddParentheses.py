from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        result = []
        for i in range(len(expression)):
            char = expression[i]
            if char in {'+', '-', '*'}:
                left_part = self.diffWaysToCompute(expression[:i])
                right_part = self.diffWaysToCompute(expression[i + 1:])
                for left in left_part:
                    for right in right_part:
                        if char == '+':
                            result.append(left + right)
                        elif char == '-':
                            result.append(left - right)
                        elif char == '*':
                            result.append(left * right)

        return result

# Unit Test
solution = Solution()
print(solution.diffWaysToCompute("2-1-1"))  # Output: [0, 2]
print(solution.diffWaysToCompute("2*3-4*5"))  # Output: [-34, -14, -10, -10, 10]
