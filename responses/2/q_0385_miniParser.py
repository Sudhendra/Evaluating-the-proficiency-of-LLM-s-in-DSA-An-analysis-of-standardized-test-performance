class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        stack = []
        num = ""
        for char in s:
            if char == "[":
                new_list = NestedInteger()
                if stack:
                    stack[-1].add(new_list)
                stack.append(new_list)
            elif char.isdigit() or char == "-":
                num += char
            elif char == ",":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                    num = ""
            elif char == "]":
                if num:
                    stack[-1].add(NestedInteger(int(num)))
                num = ""
                top = stack.pop()
                if stack:
                    stack[-1].add(top)
        return stack[0]
