class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        last_occurrence = {char: idx for idx, char in enumerate(s)}

        for idx, char in enumerate(s):
            if char in stack:
                continue
            
            while stack and char < stack[-1] and idx < last_occurrence[stack[-1]]:
                stack.pop()
            
            stack.append(char)

        return ''.join(stack)