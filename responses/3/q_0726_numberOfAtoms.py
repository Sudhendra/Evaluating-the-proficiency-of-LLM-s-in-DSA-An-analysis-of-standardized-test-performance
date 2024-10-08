from collections import Counter

class Solution:
    
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        count = Counter()
        i = 0
        
        while i < len(formula):
            if formula[i] == '(':
                stack.append(count)
                count = Counter()
                i += 1
            elif formula[i] == ')':
                i += 1
                start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                factor = int(formula[start:i] or 1)
                temp_count = count
                count = stack.pop()
                for key in temp_count:
                    count[key] += temp_count[key] * factor
            else:
                start = i
                i += 1
                while i < len(formula) and formula[i].islower():
                    i += 1
                key = formula[start:i]
                start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1
                factor = int(formula[start:i] or 1)
                count[key] += factor
        
        result = ""
        for key in sorted(count.keys()):
            result += key
            if count[key] > 1:
                result += str(count[key])
        
        return result