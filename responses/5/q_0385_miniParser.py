class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        
        i = 0
        while i < len(s):
            if s[i] == '[':
                stack.append(NestedInteger())
                i += 1
            elif s[i].isdigit() or s[i] == '-':
                j = i
                while j < len(s) and (s[j].isdigit() or s[j] == '-'):
                    j += 1
                stack[-1].add(NestedInteger(int(s[i:j])))
                i = j
            elif s[i] == ',':
                i += 1
            elif s[i] == ']':
                if len(stack) > 1:
                    top = stack.pop()
                    stack[-1].add(top)
                i += 1
        
        return stack[0] if stack else NestedInteger()
