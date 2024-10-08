class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def helper(s: str) -> NestedInteger:
            if s[0] != '[':
                return NestedInteger(int(s))
            
            stack = []
            i = 0
            while i < len(s):
                if s[i] == '[':
                    stack.append(NestedInteger())
                elif s[i] == ']':
                    if len(stack) > 1:
                        top = stack.pop()
                        stack[-1].add(top)
                elif '0' <= s[i] <= '9' or s[i] == '-':
                    j = i
                    while j < len(s) and ('0' <= s[j] <= '9' or s[j] == '-'):
                        j += 1
                    stack[-1].add(NestedInteger(int(s[i:j])))
                    i = j - 1
                i += 1

            return stack[0]

        return helper(s)