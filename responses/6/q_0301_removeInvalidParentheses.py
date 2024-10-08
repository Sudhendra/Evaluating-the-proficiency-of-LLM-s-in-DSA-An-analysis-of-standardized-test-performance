from typing import List

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s: str) -> bool:
            count = 0
            for char in s:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        def backtrack(index: int, left_count: int, right_count: int, left_removal: int, right_removal: int, expr: str) -> None:
            nonlocal ans
            if index == len(s):
                if left_removal == 0 and right_removal == 0 and is_valid(expr):
                    ans.add(expr)
                return
            
            if s[index] == '(' and left_removal > 0:
                backtrack(index + 1, left_count, right_count, left_removal - 1, right_removal, expr)
            if s[index] == ')' and right_removal > 0:
                backtrack(index + 1, left_count, right_count, left_removal, right_removal - 1, expr)
            
            expr += s[index]
            if s[index] != '(' and s[index] != ')':
                backtrack(index + 1, left_count, right_count, left_removal, right_removal, expr)
            elif s[index] == '(':
                backtrack(index + 1, left_count + 1, right_count, left_removal, right_removal, expr)
            elif s[index] == ')' and left_count > right_count:
                backtrack(index + 1, left_count, right_count + 1, left_removal, right_removal, expr)
            
        ans = set()
        left = 0
        right = 0
        for char in s:
            if char == '(':
                left += 1
            if char == ')':
                if left == 0:
                    right += 1
                else:
                    left -= 1
        
        backtrack(0, 0, 0, left, right, "")
        return list(ans)
