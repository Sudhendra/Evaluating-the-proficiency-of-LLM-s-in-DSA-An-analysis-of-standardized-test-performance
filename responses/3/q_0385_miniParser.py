class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        num = None
        i = 0

        while i < len(s):
            if s[i] == '[':
                stack.append(NestedInteger())
            elif s[i].isdigit() or s[i] == '-':
                j = i
                while j < len(s) and (s[j].isdigit() or s[j] == '-'):
                    j += 1
                num = int(s[i:j])
                stack[-1].add(NestedInteger(num))
                i = j - 1
            elif s[i] == ']':
                if len(stack) > 1:
                    last = stack.pop()
                    stack[-1].add(last)
            i += 1

        return stack[0]