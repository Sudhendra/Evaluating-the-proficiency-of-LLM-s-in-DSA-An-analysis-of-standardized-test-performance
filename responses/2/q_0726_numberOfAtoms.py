class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse_element(s):
            count = ""
            symbol = s[0]
            s = s[1:]
            while s and s[0].islower():
                symbol += s[0]
                s = s[1:]
            while s and s[0].isdigit():
                count += s[0]
                s = s[1:]
            return (symbol, int(count) if count else 1), s
        
        def parse_formula(s):
            stack = [collections.defaultdict(int)]
            i = 0
            while i < len(s):
                if s[i] == "(":
                    stack.append(collections.defaultdict(int))
                    i += 1
                elif s[i] == ")":
                    top = stack.pop()
                    i += 1
                    count = ""
                    while i < len(s) and s[i].isdigit():
                        count += s[i]
                        i += 1
                    multiplier = int(count) if count else 1
                    for symbol, num in top.items():
                        stack[-1][symbol] += num * multiplier
                else:
                    element, remaining = parse_element(s[i:])
                    stack[-1][element[0]] += element[1]
                    i += len(element[0])
            return stack[0]
        
        elements = parse_formula(formula)
        result = ""
        for element, count in sorted(elements.items()):
            result += element
            if count > 1:
                result += str(count)
        return result