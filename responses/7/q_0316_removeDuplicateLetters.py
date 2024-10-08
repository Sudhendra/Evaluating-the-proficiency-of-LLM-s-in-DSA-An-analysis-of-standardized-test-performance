class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence = {char: index for index, char in enumerate(s)}
        stack = []
        seen = set()

        for index, char in enumerate(s):
            if char in seen:
                continue
            while stack and char < stack[-1] and index < last_occurrence[stack[-1]]:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)

        return "".join(stack)
