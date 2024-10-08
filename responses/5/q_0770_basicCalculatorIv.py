from typing import List

class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        def combine(poly1, poly2, sign):
            result = {}
            for key in poly1:
                result[key] = sign * poly1[key]
            for key in poly2:
                result[key] = result.get(key, 0) + poly2[key]
            return {key: coeff for key, coeff in result.items() if coeff}

        def parse(s):
            s = s.replace('(', '( ').replace(')', ' )')
            tokens = s.split(' ')
            result = []
            stack = []
            sign = 1

            for token in tokens:
                if token == '':
                    continue
                if token in '+-':
                    sign = 1 if token == '+' else -1
                elif token == '(':
                    stack.append(sign)
                    sign = 1
                elif token == ')':
                    sign = stack.pop()
                elif token.isalpha():
                    result.append({token: sign})
                else:
                    result.append({'': int(token) * sign})

            return result

        def evaluate(expression, values):
            values = {var: val for var, val in zip(evalvars, evalints)}
            poly_stack = []
            expr_stack = []

            for token in expression.split():
                if token == '+':
                    expr_stack.append(poly_stack.pop())
                elif token == '-':
                    expr_stack.append(combine({}, poly_stack.pop(), -1))
                elif token == '*':
                    continue
                elif token == '(':
                    expr_stack.append((0, 0))
                elif token == ')':
                    if expr_stack[-1] == (0, 0):
                        expr_stack.pop()
                    else:
                        to_append = expr_stack.pop()
                        poly_stack[-1] = combine(poly_stack[-1], to_append[0], to_append[1])
                else:
                    poly_stack.append({token: 1})

            final_result = combine({}, expr_stack[0], 1)

            return sorted(['*'.join([str(final_result[key]), key]) for key in final_result], key=lambda x: (-len(x), x))

        expression = expression.replace('-', ' -').replace('+', ' +')
        parsed_expression = parse(expression)
        return evaluate(' '.join(['*'.join(val for val in term) for term in parsed_expression]), evalints)
