from typing import List

class Solution:
    """Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

    Return *a list of **unique strings** that are valid with the minimum number of removals*. You may return the answer in **any order**.
    """
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

        level = {s}
        while True:
            valid = list(filter(is_valid, level))
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

# Example usage
sol = Solution()
input_str = "()())()"
output = sol.removeInvalidParentheses(input_str)
print(output)
