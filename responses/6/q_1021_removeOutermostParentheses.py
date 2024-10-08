class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        opened = 0
        result = ""
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
