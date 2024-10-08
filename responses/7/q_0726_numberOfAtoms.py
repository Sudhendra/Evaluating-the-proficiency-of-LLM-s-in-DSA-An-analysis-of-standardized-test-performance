class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse_formula(formula: str) -> dict:
            stack = []
            elem = ''
            num = 0
            for c in formula:
                if c.isupper():
                    if elem:
                        stack.append((elem, num if num else 1))
                        elem = ''
                        num = 0
                    elem += c
                elif c.islower():
                    elem += c
                elif c.isdigit():
                    num = num * 10 + int(c)
                elif c == '(':
                    stack.append('(')
                elif c == ')':
                    if elem:
                        stack.append((elem, num if num else 1))
                        elem = ''
                        num = 0
                    temp = []
                    while stack[-1] != '(':
                        top = stack.pop()
                        if isinstance(top, tuple):
                            temp.append(top)
                        else:
                            multiplier = stack.pop()
                            for i in range(len(temp)):
                                if temp[i][1] != 1:
                                    temp[i] = (temp[i][0], temp[i][1] * multiplier)
                            stack += temp
                    stack.pop()
                else:
                    raise ValueError(f"Unexpected character: {c}")
            if elem:
                stack.append((elem, num if num else 1))
            elements = {}
            for e in stack:
                if isinstance(e, tuple):
                    if e[0] not in elements:
                        elements[e[0]] = 0
                    elements[e[0]] += e[1]
            return elements

        elements = parse_formula(formula)
        result = ''
        for elem, count in sorted(elements.items()):
            result += elem
            if count > 1:
                result += str(count)
        return result
