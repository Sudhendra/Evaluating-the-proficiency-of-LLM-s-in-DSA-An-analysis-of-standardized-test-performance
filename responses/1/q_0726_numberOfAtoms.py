from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse_formula(formula):
            stack = []
            i = 0
            while i < len(formula):
                if formula[i] == '(' or formula[i] == ')':
                    stack.append(formula[i])
                    i += 1
                elif formula[i].isupper():
                    element = formula[i]
                    i += 1
                    while i < len(formula) and formula[i].islower():
                        element += formula[i]
                        i += 1
                    stack.append(element)
                else:
                    num = ''
                    while i < len(formula) and formula[i].isdigit():
                        num += formula[i]
                        i += 1
                    stack.append(int(num))
            return stack

        def flatten_stack(stack):
            i = len(stack) - 1
            while i > 0:
                if stack[i] == ')':
                    sub_stack = []
                    while stack[-1] != '(':
                        sub_stack.append(stack.pop())
                    stack.pop()  # remove '('
                    factor = stack.pop() if i < len(stack) else 1
                    for j in range(len(sub_stack) - 1):
                        if type(sub_stack[j]) == int:
                            sub_stack[j] *= factor
                    stack.extend(sub_stack)
                i -= 1
            return stack

        stack = parse_formula(formula)
        stack = flatten_stack(stack)

        counts = Counter()
        i = 0
        while i < len(stack):
            if type(stack[i]) == str:
                element = stack[i]
                count = 1
                if i + 1 < len(stack) and type(stack[i + 1]) == int:
                    count = stack[i + 1]
                    i += 1
                counts[element] += count
            i += 1

        output = ''
        for element, count in sorted(counts.items()):
            output += element
            if count > 1:
                output += str(count)

        return output
