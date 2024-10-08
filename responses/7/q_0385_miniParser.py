from collections import deque

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':  # Only a single integer in the input
            return NestedInteger(int(s))
        
        stack = deque()
        start = 0
        
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(NestedInteger())
                start = i + 1
            elif s[i] in ',]':
                if s[start:i].lstrip('-').isdigit():
                    stack[-1].add(NestedInteger(int(s[start:i])))
                if s[i] == ']':
                    if len(stack) > 1:
                        top = stack.pop()
                        stack[-1].add(top)
        
        return stack.pop()
