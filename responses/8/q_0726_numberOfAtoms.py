from collections import Counter

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse_formula(s: str, count: int):
            stack = []
            i = 0
            while i < len(s):
                if s[i] == '(':
                    j = i
                    balance = 0
                    while i < len(s):
                        if s[i] == '(':
                            balance += 1
                        elif s[i] == ')':
                            balance -= 1
                        if balance == 0:
                            break
                        i += 1
                    subs = parse_formula(s[j+1:i], count)
                else:
                    j = i
                    i += 1
                    while i < len(s) and s[i].islower():
                        i += 1
                    atom = s[j:i]
                    j = i
                    while i < len(s) and s[i].isdigit():
                        i += 1
                    cnt = int(s[j:i] or 1)
                    subs = Counter({atom: cnt * count})
                stack.append(subs)

                j = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                count = int(s[j:i] or 1)

            res = sum(stack[::2], Counter()) + sum((x * count for x in stack[1::2]), Counter())
            return res

        counts = parse_formula(formula, 1)
        res = ''.join([f"{key}{counts[key]}" if counts[key] > 1 else key for key in sorted(counts)])

        return res
