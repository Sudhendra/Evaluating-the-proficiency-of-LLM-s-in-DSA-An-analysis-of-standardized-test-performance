from collections import deque

class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        def parse_integer(s: str) -> int:
            sign = 1
            if s[0] == '-':
                sign = -1
                s = s[1:]
            return int(s) * sign

        def build_nested_integer(token: str) -> NestedInteger:
            if '[' not in token:
                return NestedInteger(parse_integer(token))
            
            nested_list = NestedInteger()
            stack = deque()
            current = None

            for c in token:
                if c == '[':
                    new_list = NestedInteger()
                    if stack:
                        stack[-1].add(new_list)
                    stack.append(new_list)
                elif c == ']':
                    current = stack.pop()
                elif c.isdigit() or c == '-':
                    start = token.index(c)
                    end = start
                    while end < len(token) and (token[end].isdigit() or token[end] == '-'):
                        end += 1
                    new_token = token[start:end]
                    new_integer = NestedInteger(parse_integer(new_token))
                    if current is None:
                        current = new_integer
                    else:
                        current.add(new_integer)

            return current

        return build_nested_integer(s)
