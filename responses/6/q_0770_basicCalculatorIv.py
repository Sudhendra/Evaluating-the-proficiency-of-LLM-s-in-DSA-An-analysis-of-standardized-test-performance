from typing import List

class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        from collections import Counter
        import re

        def combine(expr1, expr2, op):
            if op == '+':
                return expr1 + expr2
            elif op == '-':
                return expr1 - expr2
            elif op == '*':
                return expr1 * expr2

        def evaluate(expr, eval_map):
            if expr.isdigit():
                return int(expr)
            elif expr in eval_map:
                return eval_map[expr]
            else:
                return expr

        def parse(expression):
            expression = expression.replace('(', '( ').replace(')', ' )')
            tokens = expression.split()
            stack = []
            prec = {'(': 0, '+': 1, '-': 1, '*': 2}

            for token in tokens:
                if token == '(':
                    stack.append(token)
                elif token == ')':
                    while stack[-1] != '(':
                        stack.append(combine(stack.pop(), stack.pop(), stack.pop()))
                    stack.pop()
                elif token in '+-*':
                    while stack and prec[stack[-1]] >= prec[token]:
                        stack.append(combine(stack.pop(-2), stack.pop(), stack.pop()))
                    stack.append(token)
                else:
                    stack.append(token)

            while len(stack) > 1:
                stack.append(combine(stack.pop(-2), stack.pop(), stack.pop()))

            return stack[0]

        eval_map = dict(zip(evalvars, evalints))
        variables = Counter()
        stack = []
        cur_expr = ''
        res = []

        for ch in expression:
            if ch.isalnum():
                cur_expr += ch
            else:
                if cur_expr:
                    stack.append(evaluate(cur_expr, eval_map))
                    cur_expr = ''

                if ch.isalpha():
                    stack.append(ch)
                elif ch.isdigit() or ch in '+-*':
                    stack.append(ch)
                elif ch == '(':
                    stack.append(ch)
                elif ch == ')':
                    temp = []
                    while stack[-1] != '(':
                        temp.append(stack.pop())
                    stack.pop()
                    stack.append(parse(' '.join(temp[::-1])))
        
        if cur_expr:
            stack.append(evaluate(cur_expr, eval_map))

        for item in stack:
            if isinstance(item, int):
                coeff = item
            else:
                coeff = 1

            if isinstance(item, str):
                variables[item] += coeff
        
        sorted_vars = sorted(variables.items(), key=lambda x: (-len(x[0]), x[0]))
        
        for var, coeff in sorted_vars:
            if coeff != 0:
                res.append('*'.join([str(coeff), var]))
        
        return res
