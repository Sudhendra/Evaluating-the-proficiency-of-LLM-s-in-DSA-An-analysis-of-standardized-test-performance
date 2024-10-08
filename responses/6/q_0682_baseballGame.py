from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total_sum = 0

        for op in operations:
            if op == 'C':
                total_sum -= stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
                total_sum += stack[-1]
            elif op == '+':
                new_score = stack[-1] + stack[-2]
                stack.append(new_score)
                total_sum += new_score
            else:
                score = int(op)
                stack.append(score)
                total_sum += score

        return total_sum
