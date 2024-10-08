from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [Counter()]
        i = 0
        n = len(formula)

        while i < n:
            if formula[i] == '(':
                stack.append(Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1

                j = i
                while j < n and formula[j].isdigit():
                    j += 1

                factor = int(formula[i:j] or 1)
                i = j

                for elem, cnt in top.items():
                    stack[-1][elem] += cnt * factor
            else:
                j = i + 1
                while j < n and formula[j].islower():
                    j += 1

                elem = formula[i:j]
                i = j

                while j < n and formula[j].isdigit():
                    j += 1

                stack[-1][elem] += int(formula[i:j] or 1)
                i = j

        result = ""
        for elem, count in sorted(stack[-1].items()):
            result += elem
            if count > 1:
                result += str(count)

        return result
