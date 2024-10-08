class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last_occurrence = {char: idx for idx, char in enumerate(s)}
        stack = []
        seen = set()

        for idx, char in enumerate(s):
            if char in seen:
                continue
            while stack and char < stack[-1] and idx < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
