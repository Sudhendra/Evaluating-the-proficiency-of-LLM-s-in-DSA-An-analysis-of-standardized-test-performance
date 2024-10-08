class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        opened = 0

        for char in s:
            if char == '(':
                if opened > 0:
                    result += char
                opened += 1
            else:
                opened -= 1
                if opened > 0:
                    result += char

        return result
