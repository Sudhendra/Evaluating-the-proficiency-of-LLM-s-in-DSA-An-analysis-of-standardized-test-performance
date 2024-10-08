from collections import defaultdict

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [defaultdict(int)]
        
        i = 0
        n = len(formula)
        
        while i < n:
            if formula[i] == '(':
                stack.append(defaultdict(int))
                i += 1
            elif formula[i] == ')':
                tmp = stack.pop()
                i += 1
                j = i
                while j < n and formula[j].isdigit():
                    j += 1
                multiplier = int(formula[i:j] or '1')
                for atom, count in tmp.items():
                    stack[-1][atom] += count * multiplier
                i = j
            else:
                j = i + 1
                while j < n and formula[j].islower():
                    j += 1
                atom = formula[i:j]
                i = j
                while j < n and formula[j].isdigit():
                    j += 1
                count = int(formula[i:j] or '1')
                stack[-1][atom] += count
                i = j
        
        result = ''
        for atom, count in sorted(stack[-1].items()):
            result += atom + (str(count) if count > 1 else '')
        return result
