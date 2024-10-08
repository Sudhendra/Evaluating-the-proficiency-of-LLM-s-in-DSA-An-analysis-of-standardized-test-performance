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

        def backtrack(start, left, right, open_str, result):
            if left == 0 and right == 0:
                if is_valid(open_str):
                    result.add(open_str)

            for i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]:
                    continue

                if s[i] == '(' and left > 0:
                    backtrack(i, left - 1, right, open_str + s[i], result)
                if s[i] == ')' and right > 0:
                    backtrack(i, left, right - 1, open_str + s[i], result)

        left = 0
        right = 0
        for char in s:
            if char == '(':
                left += 1
            elif char == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
        
        result = set()
        backtrack(0, left, right, "", result)
        
        return list(result)

# Example usage
sol = Solution()
print(sol.removeInvalidParentheses("()())()"))