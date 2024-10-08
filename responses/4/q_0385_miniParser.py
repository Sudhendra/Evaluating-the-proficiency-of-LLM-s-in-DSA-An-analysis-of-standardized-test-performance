class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        num = ''
        for c in s:
            if c == '[':
                stack.append(NestedInteger())
            elif c == ']':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
                top = stack.pop()
                if stack:
                    stack[-1].add(top)
                else:
                    return top
            elif c == ',':
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ''
            else:
                num += c
        return NestedInteger(int(num))
