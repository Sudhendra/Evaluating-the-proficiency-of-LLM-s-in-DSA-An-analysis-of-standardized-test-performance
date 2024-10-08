class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = ""
        open_count = 0
        for char in s:
            if char == "(":
                if open_count > 0:
                    result += char
                open_count += 1
            else:
                open_count -= 1
                if open_count > 0:
                    result += char
        return result
