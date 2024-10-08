class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        additions = 0

        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                additions += 1

        return additions + len(stack)
