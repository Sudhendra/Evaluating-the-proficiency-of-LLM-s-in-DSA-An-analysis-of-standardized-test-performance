from collections import deque

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = deque()
        start = 1
        for i in range(1, len(s)):
            if s[i] == '[':
                stack.append(NestedInteger())
                start = i + 1
            elif s[i] in ',]':
                if s[i-1].isdigit():
                    stack[-1].add(NestedInteger(int(s[start:i])))
                if s[i] == ']' and len(stack) > 1:
                    nested = stack.pop()
                    stack[-1].add(nested)
                start = i + 1

        return stack.pop()
