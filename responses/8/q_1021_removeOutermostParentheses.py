class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        opened = 0

        for char in s:
            if char == '(' and opened > 0:
                result.append(char)
            if char == ')' and opened > 1:
                result.append(char)
            opened += 1 if char == '(' else -1

        return ''.join(result)
