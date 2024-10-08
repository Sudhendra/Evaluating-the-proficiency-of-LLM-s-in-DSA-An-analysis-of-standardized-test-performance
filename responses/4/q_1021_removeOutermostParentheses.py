class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        result = []
        start = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                if len(stack) == 1:
                    result.append(s[start + 1:i])
                    start = i + 1
                stack.pop()

        return "".join(result)
