class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse(formula: str) -> dict:
            stack = []
            i = 0
            while i < len(formula):
                if formula[i] == '(':
                    stack.append('(')
                    i += 1
                elif formula[i] == ')':
                    count = 0
                    i += 1
                    while i < len(formula) and formula[i].isdigit():
                        count = count * 10 + ord(formula[i]) - ord('0')
                        i += 1
                    stack.pop()
                    for key, value in stack.pop().items():
                        stack[-1][key] = stack[-1].get(key, 0) + value * count
                    i += 1
                else:
                    j = i
                    i += 1
                    while i < len(formula) and formula[i].islower():
                        i += 1
                    key = formula[j:i]
                    count = 0
                    while i < len(formula) and formula[i].isdigit():
                        count = count * 10 + ord(formula[i]) - ord('0')
                        i += 1
                    count = max(1, count)
                    stack.append({key: count})
            result = {}
            for elem in stack:
                for key, value in elem.items():
                    result[key] = result.get(key, 0) + value
            return result

        counts = parse(formula)
        result = ""
        for key in sorted(counts.keys()):
            result += key
            if counts[key] > 1:
                result += str(counts[key])
        return result
