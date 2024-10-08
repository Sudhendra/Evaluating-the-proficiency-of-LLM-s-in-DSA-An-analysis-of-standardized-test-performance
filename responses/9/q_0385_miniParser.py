class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))
        
        stack = []
        start = 0
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(NestedInteger())
                start = i + 1
            elif s[i] in ',]':
                if start < i:
                    stack[-1].add(NestedInteger(int(s[start:i])))
                if s[i] == ']' and len(stack) > 1:
                    cur = stack.pop()
                    stack[-1].add(cur)
                start = i + 1

        return stack[0]
