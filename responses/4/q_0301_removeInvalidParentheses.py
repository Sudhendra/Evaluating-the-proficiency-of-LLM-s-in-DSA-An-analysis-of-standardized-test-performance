from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s):
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        def backtrack(index, left_count, right_count, left_removed, right_removed, expr):
            if index == len(s):
                if left_removed == 0 and right_removed == 0 and is_valid(expr):
                    result.add(expr)
                return

            if s[index] == '(' and left_removed > 0:
                backtrack(index + 1, left_count, right_count, left_removed - 1, right_removed, expr)
            elif s[index] == ')' and right_removed > 0:
                backtrack(index + 1, left_count, right_count, left_removed, right_removed - 1, expr)

            if s[index] != '(' and s[index] != ')':
                backtrack(index + 1, left_count, right_count, left_removed, right_removed, expr + s[index])
            else:
                if s[index] == '(':
                    backtrack(index + 1, left_count + 1, right_count, left_removed, right_removed, expr + '(')
                elif s[index] == ')' and left_count > right_count:
                    backtrack(index + 1, left_count, right_count + 1, left_removed, right_removed, expr + ')')

                backtrack(index + 1, left_count, right_count, left_removed, right_removed, expr)
        
        result = set()
        left_removed, right_removed = 0, 0
        for char in s:
            if char == '(':
                left_removed += 1
            elif char == ')':
                if left_removed == 0:
                    right_removed += 1
                else:
                    left_removed -= 1
        
        backtrack(0, 0, 0, left_removed, right_removed, "")
        return list(result)
